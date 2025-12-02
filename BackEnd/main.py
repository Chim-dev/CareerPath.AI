from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import os
import re
from dotenv import load_dotenv
import google.generativeai as genai

# ============ LOAD ENV ============
load_dotenv()

# ============ FASTAPI APP ============
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173","https://careerai-sigma.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============ MODEL DEFINISI ============
class CareerAssessment(BaseModel):
    category: str
    gender: str
    questions: List[str]     # <==== TAMBAHAN
    answers: List[str]

class AnalysisResult(BaseModel):
    analysis: str
    career_recommendations: List[str]
    development_advice: str
    confidence_score: float

# ============ CLEAN MARKDOWN ============
def clean_markdown(text: str) -> str:
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
    text = re.sub(r'\*(.*?)\*', r'\1', text)
    text = re.sub(r'[_~`]', '', text)

    # ❗ penting: jangan hilangkan newline
    text = re.sub(r'[ \t]+', ' ', text)

    return text.strip()


# ============ EXTRACT KARIR ============
def extract_careers(text: str) -> List[str]:
    pattern = r'\d+\s*[\.\)]\s*([A-Za-zÀ-ÿ\'\-\s/&]+)'
    careers = re.findall(pattern, text)
    return [c.strip() for c in careers][:3]

# ============ EXTRACT SARAN ============
def extract_advice(text: str) -> str:
    match = re.search(r"SARAN PENGEMBANGAN DIRI:(.*)", text, re.DOTALL)
    return match.group(1).strip() if match else ""

# ============ CONFIG GEMINI ============
GEMINI_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_KEY:
    raise RuntimeError("❌ GEMINI_API_KEY tidak ditemukan di .env")

genai.configure(api_key=GEMINI_KEY)
MODEL_NAME = "gemini-2.5-flash"

# ============ ENDPOINT UTAMA ============
@app.post("/analyze", response_model=AnalysisResult)
async def analyze_career(assessment: CareerAssessment):

    # --- Deteksi minat Game Development ---
    game_keywords = ["game", "unity", "unreal", "gamedev", "developer game", "game designer"]
    user_text = " ".join(assessment.answers).lower()
    game_interest = any(kw in user_text for kw in game_keywords)

    game_instruction = ""
    if game_interest:
        game_instruction = """
Penting: Klien menunjukkan minat pada Game Development. Maka rekomendasi karier
wajib berfokus pada bidang seperti:
- Game Developer (Unity atau Unreal Engine)
- Gameplay Programmer
- Game Designer
- Technical Game Designer
- Game AI Engineer
"""

    # --- Gabungkan soal + jawaban ---
    qna_formatted = "\n".join(
        [
            f"{i+1}. {assessment.questions[i]}\n   Jawaban: {assessment.answers[i]}"
            for i in range(len(assessment.questions))
        ]
    )

    # --- PROMPT FINAL ---
    prompt = f"""
Kamu adalah konsultan karier profesional di Indonesia.

Gunakan bahasa informal, santai tapi tetap sopan (seperti ngobrol ke user).

Format output WAJIB persis seperti ini:

ANALISIS:
(isi 3-5 kalimat)

SARAN PENGEMBANGAN DIRI:
(isi 1-2 kalimat)

REKOMENDASI KARIER:
1. Karier pertama (yang paling sesuai)
2. Karier kedua (pilihan alternatif)
3. Karier ketiga (pilihan alternatif)
4. Karier keempat
5. Karier kelima


Dilarang menggunakan simbol markdown seperti **, *, _, ~, atau ```.

{game_instruction}

Kategori Penilaian: {assessment.category}
Jenis Kelamin Klien: {assessment.gender}

Soal dan Jawaban Klien:
{qna_formatted}
""".strip()

    try:
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(prompt)

        text = clean_markdown(response.text)
        careers = extract_careers(text)
        advice = extract_advice(text)

        return AnalysisResult(
            analysis=text,
            career_recommendations=careers,
            development_advice=advice,
            confidence_score=0.95 if len(text) > 200 else 0.80,
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server Error: {e}")

# ============ ROOT ============
@app.get("/")
def root():
    return {"status": "Backend OK", "model": MODEL_NAME, "endpoint": "/analyze"}

# ============ RUN ============
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
