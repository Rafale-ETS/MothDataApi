# Generated by Django 3.1.1 on 2020-09-29 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200929_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accelerometerdata',
            name='data_point',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='accel_data', to='api.datapoint'),
        ),
        migrations.AlterField(
            model_name='gpsdata',
            name='data_point',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='gps_data', to='api.datapoint'),
        ),
        migrations.AlterField(
            model_name='gyroscopedata',
            name='data_point',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='gyro_data', to='api.datapoint'),
        ),
        migrations.AlterField(
            model_name='temperaturedata',
            name='data_point',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='temp_data', to='api.datapoint'),
        ),
        migrations.AlterField(
            model_name='waterdata',
            name='data_point',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='water_data', to='api.datapoint'),
        ),
        migrations.AlterField(
            model_name='winddata',
            name='data_point',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='wind_data', to='api.datapoint'),
        ),
    ]
