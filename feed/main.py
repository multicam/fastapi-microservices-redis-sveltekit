from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware
from starlette.middleware.gzip import GZipMiddleware

from src.router import router

origins = [
    'http://jmbox.local:3000',
    'http://localhost:3000',
    '*'
]


app = FastAPI()
app.add_middleware(GZipMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get("/")
def index():
    return {"Hello": "Feed"}


print('----| feed running...')
app.include_router(router)
