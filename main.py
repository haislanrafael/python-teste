from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "hello word"}

@app.get("/teste1")
async def funcaoteste():
    return {"teste": "deu certo"}

