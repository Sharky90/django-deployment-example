# Generated by Django 2.2.5 on 2020-01-11 12:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200111_1300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='create_date',
        ),
        migrations.AddField(
            model_name='comment',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 1, 11, 12, 1, 43, 397208, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 11, 12, 1, 43, 396204, tzinfo=utc)),
        ),
    ]
