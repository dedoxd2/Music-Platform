from __future__ import absolute_import, unicode_literals
from datetime import timedelta
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'musicplatform.settings')
app = Celery("musicplatform")
app.conf.enable_utc = True
app.config_from_object(settings, namespace='CELERY')
# Celery Beat Settings
app.conf.beat_schedule = {
    'send_inactivity_reminder_emails':
    {
        'task': 'artists.tasks.send_inactivity_reminder_emails',

        'schedule': timedelta(seconds=10),  # hours = 24
    },
}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
