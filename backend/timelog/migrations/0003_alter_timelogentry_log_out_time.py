# Generated by Django 4.1.5 on 2023-01-07 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timelog', '0002_userlivestatus_active_log_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timelogentry',
            name='log_out_time',
            field=models.TimeField(null=True),
        ),
    ]