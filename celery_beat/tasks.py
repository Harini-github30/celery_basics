import os
from dotenv import load_dotenv
from celery import Celery
from celery.schedules import crontab

load_dotenv()

broker_url = os.getenv("broker_url")
app = Celery('tasks',broker=broker_url)

@app.task
def welcome(): return 'Hi'

@app.task
def multiply(x, y): return x*y


app.conf.beat_schedule = {
    'print-every-minute': {
        'task': 'tasks.welcome',
        'schedule': crontab(), ##every minute
    },
    'multiple': {
        'task': 'tasks.multiply',
        'schedule': crontab(minute='*/2'), ## evry two minute 
        ##argumetns of crontab(minute='*', hour='*', day_of_month='*', month_of_year='*', day_of_week='*'),
        'args': (2,3)
    },
}