import time
from src.database import redis
from src.models import Order


def main():
  key = 'refund_order'
  group = 'payment-group'

  try:
    redis.xgroup_create(key, group)
  except:
    print('Group already exists!')

  while True:
    try:
      results = redis.xreadgroup(group, key, {key: '>'}, None)
      if results != []:
        print(results)
        for r in results:
          obj = r[1][0][1]
          order = Order.get(obj['pk'])
          if order:
            print(order)
            order.status = 'refunded'
            order.save()

    except Exception as e:
      print(str(e))
    time.sleep(1)


if __name__ == '__main__':
  main()
