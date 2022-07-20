from functools import lru_cache
from fastapi import APIRouter, Body
from fastapi.background import BackgroundTasks
import requests, time

from .models import Order
from .config import Settings
from .database import redis

router = APIRouter()


@lru_cache()
def get_settings():
  return Settings()


@router.post('/orders', status_code=201)
async def create_order(background_tasks: BackgroundTasks, product_id: str = Body(...), quantity: int = Body(...)):
  res = requests.get(
      f"{get_settings().inventory_server_url}/products/{product_id}"
  )
  product = res.json()
  print(product)
  order = Order(
      product_id=product_id,
      price=product['price'],
      fee=0.2 * product['price'],
      total=1.2 * product['price'],
      quantity=quantity,
      status="pending"
  )
  order.save()

  background_tasks.add_task(order_completed, order)

  return order


@router.get('/orders')
def get_order():
  return [Order.get(pk) for pk in Order.all_pks()]


@router.get('/orders/{order_id}')
def get_order(order_id: str):
  return Order.get(order_id)


def order_completed(order: Order):
  time.sleep(5)
  order.status = "completed"
  order.save()
  redis.xadd('order_completed', order.dict(), '*')
