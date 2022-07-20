import time
from src.database import redis
from src.models import Product


def main():
    key = 'order_completed'
    group = 'inventory-group'

    try:
        redis.xgroup_create(key, group)
    except:
        print('Group already exists!')

    while True:
        try:
            results = redis.xreadgroup(group, key, {key: '>'}, None)
            if results:
                print(results)
                for r in results:
                    obj = r[1][0][1]
                    try:
                        product = Product.get(obj['product_id'])
                        print(product)
                        product.quantity = product.quantity - int(obj['quantity'])
                        product.save()
                    except:
                        print('Product does not exists. Refund order.')
                        redis.xadd('refund_order', obj, '*')
        except Exception as e:
            print(str(e))
        time.sleep(1)


if __name__ == '__main__':
    main()
