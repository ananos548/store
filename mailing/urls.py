from django.urls import path
from .views import MailingView


urlpatterns = [
    path('mailing', MailingView.as_view(), name='mailing')
]
