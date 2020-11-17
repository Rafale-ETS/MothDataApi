# Generated by Django 3.1.1 on 2020-09-29 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200929_1324'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accelerometerdata',
            old_name='acc_time',
            new_name='time',
        ),
        migrations.RenameField(
            model_name='gpsdata',
            old_name='gps_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='gpsdata',
            old_name='gps_time',
            new_name='time',
        ),
        migrations.RenameField(
            model_name='gyroscopedata',
            old_name='gyro_time',
            new_name='time',
        ),
        migrations.RenameField(
            model_name='temperaturedata',
            old_name='temp_time',
            new_name='time',
        ),
        migrations.RenameField(
            model_name='waterdata',
            old_name='water_time',
            new_name='time',
        ),
        migrations.RenameField(
            model_name='winddata',
            old_name='anemo_time',
            new_name='time',
        ),
        migrations.RemoveField(
            model_name='datapoint',
            name='accel_data',
        ),
        migrations.RemoveField(
            model_name='datapoint',
            name='gps_data',
        ),
        migrations.RemoveField(
            model_name='datapoint',
            name='gyro_data',
        ),
        migrations.RemoveField(
            model_name='datapoint',
            name='temp_data',
        ),
        migrations.RemoveField(
            model_name='datapoint',
            name='water_data',
        ),
        migrations.RemoveField(
            model_name='datapoint',
            name='wind_data',
        ),
        migrations.AddField(
            model_name='accelerometerdata',
            name='data_point',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='accel_data', to='api.datapoint'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gpsdata',
            name='data_point',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='gps_data', to='api.datapoint'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gyroscopedata',
            name='data_point',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='gyro_data', to='api.datapoint'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='temperaturedata',
            name='data_point',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='temp_data', to='api.datapoint'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='waterdata',
            name='data_point',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='water_data', to='api.datapoint'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='winddata',
            name='data_point',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='wind_data', to='api.datapoint'),
            preserve_default=False,
        ),
    ]