# Generated by Django 3.0.10 on 2020-11-27 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0006_auto_20201127_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timestep',
            name='feels_like_temperature',
            field=models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Feels like'),
        ),
    ]
