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
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============ MODEL DEFINISI ============
class CareerAssessment(BaseModel):
    category: str
    gender: str
    answers: List[str]

class AnalysisResult(BaseModel):
    analysis: str
    career_recommendations: List[str]
    confidence_score: float

# ============ HELPER ============
def extract_careers_from_text(text: str) -> List[str]:
    pattern = r'\d+[\.)]\s*([A-Z][A-Za-z\s/&-]+)'
    matches = re.findall(pattern, text)
    return [m.strip() for m in matches][:5] if matches else ["(AI tidak mendeteksi karier)"]

# ============ CONFIG GEMINI ============
GEMINI_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_KEY:
    raise RuntimeError("❌ GEMINI_API_KEY tidak ditemukan di file .env")

genai.configure(api_key=GEMINI_KEY)

MODEL_NAME = "gemini-2.5-flash"

# ============ ENDPOINT UTAMA ============
@app.post("/analyze", response_model=AnalysisResult)
async def analyze_career(assessment: CareerAssessment):

    prompt = f"""
Kamu adalah konsultan karier profesional berpengalaman di Indonesia.
Berikut data klien:

Jenis Kelamin: {assessment.gender}
Kategori Minat: {assessment.category}

Jawaban Assessment:
{chr(10).join([f"{i+1}. {ans}" for i, ans in enumerate(assessment.answers)])}

Tugasmu:
1. Analisis kepribadian dan minat klien (3-4 kalimat)
2. Berikan 3 rekomendasi karier paling cocok (format daftar bernomor)
3. Tambahkan saran pengembangan diri singkat (1-2 kalimat)
Gunakan Bahasa Indonesia profesional.
"""

    try:
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(prompt)
        text = response.text.strip()

        careers = extract_careers_from_text(text)

        return AnalysisResult(
            analysis=text,
            career_recommendations=careers[:3],
            confidence_score=0.9 if len(text) > 200 else 0.7,
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error dari server: {e}")

# ============ ROUTES ============
@app.get("/")
def root():
    return {"status": "✅ Backend aktif", "model": MODEL_NAME, "endpoint": "/analyze"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
