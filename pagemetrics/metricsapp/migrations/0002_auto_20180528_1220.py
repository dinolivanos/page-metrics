# Generated by Django 2.0.5 on 2018-05-28 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metricsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='status_date',
            field=models.DateTimeField(),
        ),
    ]
