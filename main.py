from fastapi import FastAPI
import random


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "hello word"}

@app.get("/teste1")
async def funcaoteste():
    return {"teste": True, "deu certo": random.randint(0,1000)}




