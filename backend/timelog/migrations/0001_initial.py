# Generated by Django 4.1.5 on 2023-01-07 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TimeLogEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_date', models.DateField()),
                ('log_in_time', models.TimeField()),
                ('log_out_time', models.TimeField()),
                ('log_state', models.IntegerField(choices=[(0, 'unsettled'), (1, 'settled')])),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('login_name', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('sap_id', models.CharField(max_length=10, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email_id', models.EmailField(max_length=100)),
                ('status', models.IntegerField(choices=[(0, 'inactive'), (1, 'active')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='UserTimeSummary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('net_working_time', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='timelog.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserTimeRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('mandatory_work_time', models.IntegerField()),
                ('mandatory_break_time', models.IntegerField()),
                ('total_work_time_for_day', models.IntegerField()),
                ('log_entries', models.ManyToManyField(to='timelog.timelogentry')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timelog.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserLiveStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField()),
                ('live_state', models.IntegerField(choices=[(0, 'out'), (1, 'in')])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='timelog.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserDefault',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mandatory_break_time', models.IntegerField()),
                ('mandatory_working_time_per_day', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='timelog.user')),
            ],
        ),
        migrations.AddField(
            model_name='timelogentry',
            name='log_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timelog.user'),
        ),
    ]
