To start the celery worker two diff ways are there:
---> celery -A filename worker --loglevel=info
        this command should be given in terminal to trigger the worker of the job in the particular file
---> Or the below code snippet can be given in the main module file and run the file 
if __name__ == '__main__':
    args = ['worker', '--loglevel=INFO']
    app.worker_main(argv=args)

>> python3 filename.py -->this will trigger the celery worker

To execute the work:
 call the function by using:  func_name.delay(arg1,arg2...)

In redis to view the data that is stored we have to use redis-cli

$ redis-cli -n db_no
127.0.0.1:6379> keys *
1) "celery-task-meta-some-alpha-numeric-string" (key for the data stored)
2) "celery-task-meta-some-alpha-numeric-string"
127.0.0.1:6379> get celery-task-meta-some-alpha-numeric-string



CELERY BEAT

celery beat is more like a cronjob scheduler that makes the job to run periodically

argumetns of crontab ---> crontab(minute='', hour='', day_of_month='', month_of_year='', day_of_week=''),
  
to use celery beat in a normal python function without django 
use the command   "celery -A filename beat --loglevel=info"
