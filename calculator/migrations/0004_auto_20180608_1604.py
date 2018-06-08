# Generated by Django 2.0.5 on 2018-06-08 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0003_server_camera_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='camera',
            name='camera_address',
        ),
        migrations.RemoveField(
            model_name='camera',
            name='delete_type',
        ),
        migrations.RemoveField(
            model_name='camera',
            name='rec_enabled',
        ),
        migrations.RemoveField(
            model_name='server',
            name='camera_count',
        ),
        migrations.RemoveField(
            model_name='server',
            name='server_status',
        ),
        migrations.AlterField(
            model_name='camera',
            name='assigned_space',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='server',
            name='total_space',
            field=models.IntegerField(max_length=20),
        ),
    ]
