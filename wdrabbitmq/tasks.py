import os
from dotenv import load_dotenv
from celery import Celery

load_dotenv()

broker_url = os.getenv("broker_url")
app = Celery('tasks',broker=broker_url)

@app.task
def multiply(x, y): return x*y

if __name__ == '__main__':
    args = ['worker', '--loglevel=INFO']
    app.worker_main(argv=args)