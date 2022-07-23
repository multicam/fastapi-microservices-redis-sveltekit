import datetime

from fastapi import APIRouter
import json

router = APIRouter()


@router.get("/")
def read_root():
    return {"Hello": "Feed"}


@router.get('/feed/{day}')
def get_feed(day):
    print(':: list', day)
    return [{"id": 1}, {"id": 2}, {"id": 3}, {"id": 4}]
