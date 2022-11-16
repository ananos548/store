from django.db import models
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='media', null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default='-')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='media', null=True)
    published_at = models.DateField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.name}'
