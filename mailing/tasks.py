from store_project.celery import app

from .service import send


@app.task
def send_spam_email(email):
    send(email)
