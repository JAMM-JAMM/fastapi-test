from fastapi import FastAPI
from .routers import customers


app = FastAPI()

app.include_router(customers.router)

@app.get("/")
async def root():
    return {"message": "Main"}