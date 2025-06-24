from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["ai-communicator-bot.vercel.app"],  # 👈 можеш вказати конкретну адресу замість "*"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def read_root():
    return {"message": "Привіт! FastAPI працює&&& 🎉"}

class NameRequest(BaseModel):
    name: str




@app.post("/create-message/")
async def create_message(data: NameRequest):
    print(f"Отримано ім’я: {data.name}")  # <--- тут бачиш запит у логах
    return {"message": f"{data.name} створив новий код"}
