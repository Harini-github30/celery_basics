from celery import Celery

app = Celery('tasks', msgbroker='redis://localhost:6379/0',backend='redis://localhost:6379/1')

##backend connection is not necessary until some data is stored in redis
##6379 is the port in which redis runs

@app.task
def add(x, y):
    return x + y
