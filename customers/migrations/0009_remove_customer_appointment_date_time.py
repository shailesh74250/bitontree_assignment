# Generated by Django 3.0.1 on 2019-12-25 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0008_auto_20191225_0924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='appointment_date_time',
        ),
    ]
