from redis_om import get_redis_connection
from .config import Settings

settings = Settings()

redis = get_redis_connection(
    host=settings.redis_host,
    port=settings.redis_port,
    db=3,
    decode_responses=True
)
