import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Success! The API is working."}

