# Generated by Django 4.1.5 on 2023-01-03 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timelog', '0007_alter_timelogentry_log_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlivestatus',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='timelog.user'),
        ),
    ]
