from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_root():
    return "Welcome to API written in python"
