import os
from dotenv import load_dotenv
from celery import Celery


load_dotenv()

broker_url = os.getenv("broker_url")
app = Celery('tasks',broker=broker_url)

app.config_from_object('celeryconfig')  ##configure celeryconfig.py

@app.task
def welcome(): return 'Hi'

@app.task
def multiply(x, y): return x*y


# app.conf.beat_schedule = {
#     'print-every-minute': {
#         'task': 'tasks.welcome',
#         'schedule': crontab(), ##every minute
#     },
#     'multiple': {
#         'task': 'tasks.multiply',
#         'schedule': crontab(minute='*/2'), ## evry two minute 
#         'args': (2,3)
#     },
# }