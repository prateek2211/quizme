# Generated by Django 2.2.2 on 2019-06-25 17:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('problems', '0002_auto_20190625_1742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='author',
        ),
        migrations.AddField(
            model_name='problem',
            name='author',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
