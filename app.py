
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return { "FastAPI template app": "Welcome to FastAPI template app" }
