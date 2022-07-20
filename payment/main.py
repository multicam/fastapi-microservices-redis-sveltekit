from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.router import router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get("/")
def index():
  return {"Hello": "payment"}


app.include_router(router)
