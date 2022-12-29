# Generated by Django 4.1.4 on 2022-12-29 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timelog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDefaults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mandatory_break_time', models.IntegerField()),
                ('mandatory_working_time_per_day', models.IntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timelog.user')),
            ],
        ),
    ]
