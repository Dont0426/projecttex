# Generated by Django 4.1.1 on 2022-09-13 15:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('femitex', '0002_alter_post_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 13, 15, 22, 8, 14216)),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='My title', max_length=50),
        ),
    ]
