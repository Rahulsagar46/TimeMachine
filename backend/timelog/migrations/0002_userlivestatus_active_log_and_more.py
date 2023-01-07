# Generated by Django 4.1.5 on 2023-01-07 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timelog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlivestatus',
            name='active_log',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='usertimerecord',
            name='log_entries',
            field=models.ManyToManyField(default=[], to='timelog.timelogentry'),
        ),
    ]