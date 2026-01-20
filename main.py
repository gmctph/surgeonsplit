main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/calculate")
def calculate(a: float, b: float):
    return {
        "sum": a + b,
        "product": a * b
    }
