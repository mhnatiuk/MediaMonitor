from celery import Celery
import spider
app = Celery('stats', broker="mongodb://localhost:27017/celerybroker", backend="mongodb")
app.config_from_object("celeryconfig")

@app.task
def collect_stats():
    spider.get_facebook_and_twitter_stats()

 


