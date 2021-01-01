# Generated by Django 3.0.10 on 2020-10-29 09:36

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Station Name')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Station Latitude')),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Station Latitude')),
                ('altitude', models.IntegerField(verbose_name='Station Altitude')),
                ('type', models.CharField(max_length=3, verbose_name='Station Type')),
                ('RFid', models.CharField(max_length=2, verbose_name='Station RFid')),
                ('phone', models.IntegerField(verbose_name='Station Phone')),
            ],
        ),
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reading_time', models.DateTimeField(verbose_name='Reading Time')),
                ('wind_dir', models.IntegerField(validators=[django.core.validators.MaxValueValidator(360), django.core.validators.MinValueValidator(0)], verbose_name='Wind Direction')),
                ('wind_speed', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Wind Speed')),
                ('wind_gust', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Wind Gust')),
                ('wind_gust_dir', models.IntegerField(validators=[django.core.validators.MaxValueValidator(360), django.core.validators.MinValueValidator(0)], verbose_name='Wind Direction')),
                ('wind_speed_avg2m', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Wind Speed 2m Average')),
                ('wind_gust_10m', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Wind Gust 10 minutes')),
                ('wind_gust_dir_10m', models.IntegerField(validators=[django.core.validators.MaxValueValidator(360), django.core.validators.MinValueValidator(0)], verbose_name='Wind Gust Direction 10m')),
                ('humidity', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Relative Humidity')),
                ('temperature', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Temperature Centigrade')),
                ('rain_1h', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Rain Past Hour')),
                ('rain_today', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Rain Today')),
                ('rain_since_last', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Rain Since Last Reading')),
                ('bar_uncorrected', models.FloatField(verbose_name='Uncorrected pressure')),
                ('bar_corrected', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='Barometer (corrected)')),
                ('battery', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True, verbose_name='Battery')),
                ('light', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True, verbose_name='Battery')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather.Station')),
            ],
        ),
    ]
