# Generated by Django 2.1.1 on 2018-11-18 11:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='todo',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 18, 17, 23, 23, 192040)),
        ),
        migrations.AlterField(
            model_name='todo',
            name='todo_desc',
            field=models.CharField(max_length=40),
        ),
    ]