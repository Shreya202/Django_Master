# Generated by Django 3.1.7 on 2021-03-14 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruit_app', '0006_delete_panelistschedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='PanelistSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=70)),
                ('Available_from', models.DateTimeField()),
            ],
        ),
    ]
