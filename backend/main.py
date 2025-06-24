from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Привіт! FastAPI працює 🎉"}

class NameRequest(BaseModel):
    name: str

@app.post("/create-message/")
def create_message(data: NameRequest):
    return {"message": f"{data.name} створив новий код"}
