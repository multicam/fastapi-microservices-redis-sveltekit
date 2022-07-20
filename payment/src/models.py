from redis_om import HashModel
from .database import redis


class Order(HashModel):
  product_id: str
  price: float
  fee: float
  total: float
  quantity: int
  status: str  # pending | completed | refunded

  def __str__(self):
    return f"Order(id={self.pk!r}, product_id={self.product_id!r}, price={self.price!r}, fee={self.fee!r}, total={self.total!r}, quantity={self.quantity!r}, status={self.status!r})"

  class Meta:
    database = redis


# def format_order(pk: str):
#   order = Order.get(pk)
#   return {}
