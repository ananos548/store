# Generated by Django 4.0.7 on 2022-11-13 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='picture',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]