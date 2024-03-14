from celery.schedules import crontab
CELERYBEAT_SCHEDULE = {
    'print-every-minute': {
        'task': 'tasks.welcome',
        'schedule': crontab(), ##every minute
    },
    'multiple': {
        'task': 'tasks.multiply',
        'schedule': crontab(minute='*/2'), ## evry two minute 
        'args': (2,3)
    },
}