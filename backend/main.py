from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Привіт! FastAPI працює 🎉"}

class NameRequest(BaseModel):
    name: str




@app.post("/create-message/")
async def create_message(data: NameRequest):
    print(f"Отримано ім’я: {data.name}")  # <--- тут бачиш запит у логах
    return {"message": f"{data.name} створив новий код"}
