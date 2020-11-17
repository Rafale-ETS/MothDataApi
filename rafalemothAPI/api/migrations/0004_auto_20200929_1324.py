# Generated by Django 3.1.1 on 2020-09-29 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200917_1328'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datapoint',
            old_name='gpsdata',
            new_name='gps_data',
        ),
        migrations.RemoveField(
            model_name='accelerometerdata',
            name='datapoint',
        ),
        migrations.RemoveField(
            model_name='gyroscopedata',
            name='datapoint',
        ),
        migrations.RemoveField(
            model_name='temperaturedata',
            name='datapoint',
        ),
        migrations.RemoveField(
            model_name='waterdata',
            name='datapoint',
        ),
        migrations.RemoveField(
            model_name='winddata',
            name='datapoint',
        ),
        migrations.AddField(
            model_name='datapoint',
            name='accel_data',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.accelerometerdata'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datapoint',
            name='gyro_data',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.gyroscopedata'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datapoint',
            name='temp_data',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.temperaturedata'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datapoint',
            name='water_data',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.waterdata'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datapoint',
            name='wind_data',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.winddata'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='accelerometerdata',
            name='acc_time',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='accelerometerdata',
            name='x',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='accelerometerdata',
            name='y',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='accelerometerdata',
            name='z',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='gyroscopedata',
            name='gyro_time',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='gyroscopedata',
            name='pitch',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='gyroscopedata',
            name='roll',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='gyroscopedata',
            name='yaw',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='temperaturedata',
            name='air_temperature',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='temperaturedata',
            name='battery_temperature',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='temperaturedata',
            name='device_temperature',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='temperaturedata',
            name='temp_time',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='temperaturedata',
            name='water_temperature',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='waterdata',
            name='speed',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='waterdata',
            name='water_time',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='winddata',
            name='anemo_time',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='winddata',
            name='angle',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='winddata',
            name='speed',
            field=models.FloatField(null=True),
        ),
    ]