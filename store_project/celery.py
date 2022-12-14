import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTING_MODULE', 'store_project.settings')

app = Celery('store_project')
app.config_from_object('django.conf:settings', namespace='CELERY')  # Celery будет прочитывать переменные начинающиеся с Celery в settings.py
app.autodiscover_tasks()    # Автоматически подсыплять tasks
