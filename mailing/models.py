from django.db import models


class Mailing(models.Model):
    """ Подписка на рассылку"""
    email = models.EmailField(unique=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
