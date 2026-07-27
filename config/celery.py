import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Periodic tasks (додамо задачі після Block 4)
app.conf.beat_schedule = {
    'update-currency-rates-daily': {
        'task': 'apps.cars.tasks.update_currency_rates',
        'schedule': crontab(hour=9, minute=0),
    },
}

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')