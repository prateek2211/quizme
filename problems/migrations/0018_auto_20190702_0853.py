# Generated by Django 2.2.2 on 2019-07-02 08:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0017_problem_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='solvers',
            field=models.ManyToManyField(blank=True, related_name='solves', to=settings.AUTH_USER_MODEL),
        ),
    ]