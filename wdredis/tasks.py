from celery import Celery
import os
from dotenv import load_dotenv

load_dotenv()
redis_broker = os.getenv("redis_broker")
redis_backend = os.getenv("redis_backend")

app = Celery('tasks', msgbroker=redis_broker,backend=redis_backend)

##backend connection is not necessary until some data is stored in redis
##6379 is the port in which redis runs

@app.task
def add(x, y):
    return x + y
