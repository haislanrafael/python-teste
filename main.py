from fastapi import FastAPI

app = FastAPI()

@app.get("/hellow word")
async def root():
    return {"message": "hello word"}

@app.get("/funcaoteste")
async def funcaoteste():
    return {"teste": "deu certo,haha"}

