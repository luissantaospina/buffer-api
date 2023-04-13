import redis
import os
from dotenv import load_dotenv

load_dotenv()

redis_cache = redis.Redis(
    host=os.environ.get("RD_HOST", ""),
    port=os.environ.get("RD_PORT", "")
)
