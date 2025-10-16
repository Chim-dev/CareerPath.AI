from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
from database import db, cursor

app = FastAPI()

# model AI
model = pipeline("text2text-generation", model="google/flan-t5-base")

class TestData(BaseModel):
    answers: list[str]
    category: str
    user_id: int | None = None

@app.post("/analyze")
def analyze(data: TestData):
    prompt = f"""
    Kamu adalah konselor karier profesional.
    Berdasarkan hasil tes berikut:
    Kategori: {data.category}
    Jawaban: {', '.join(data.answers)}

    Berikan analisis mendalam mengenai kepribadian dan rekomendasi karier pengguna.
    """
    result = model(prompt, max_length=200)[0]["generated_text"]

    if data.user_id:
        cursor.execute(
            "INSERT INTO results (user_id, category, result_text) VALUES (%s, %s, %s)",
            (data.user_id, data.category, result)
        )
        db.commit()

    return {"analysis": result}
