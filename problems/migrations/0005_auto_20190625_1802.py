# Generated by Django 2.2.2 on 2019-06-25 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0004_auto_20190625_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='statement',
            field=models.TextField(),
        ),
    ]
