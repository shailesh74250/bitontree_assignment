# Generated by Django 3.0.1 on 2019-12-25 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_auto_20191225_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='appointment_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='appointment_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
