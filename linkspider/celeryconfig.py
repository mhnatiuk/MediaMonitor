from datetime import timedelta

CELERY_TIMEZONE = "Europe/Warsaw"
DEBUG=False
BROKER_URL = 'amqp://'
#CELERY_RESULT_BACKEND = 'amqp://'
CELERYD_CONCURRENCY =2
CELERY_ENABLE_UTC = True
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT=['json']


CELERYBEAT_SCHEDULE = {
	'crawl-every-30-minutes': { 
		'task' : 'tasks.crawl',
		'schedule' : timedelta(minutes=30),
		},
     'update-stats': {
        'task' : 'tasks.get_and_update_stats',
        'schedule': timedelta(minutes=30),
     },
    }


"""
'crawl-onet-every-30-minutes': { 
		'task' : 'tasks.crawl_onet',
		'schedule' : timedelta(minutes=30),
		},
	'check-stats-every-55-minutes': {
		'task' : 'tasks.check_stats',
		'schedule' : timedelta(minutes=60),
		},

"""


