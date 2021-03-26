# Generated by Django 3.1.7 on 2021-03-13 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruit_app', '0004_auto_20210312_1929'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Candidate_Name', models.CharField(max_length=70)),
                ('Skill_Category', models.CharField(choices=[('JAVA', 'JAVA'), ('PYTHON', 'PYTHON'), ('FULL STACK', 'FULL STACK'), ('BACKEND', 'BACKEND')], max_length=20)),
                ('Account', models.CharField(max_length=50)),
                ('Grade', models.CharField(choices=[('IS1', 'IS1'), ('IS2', 'IS2'), ('IS3', 'IS3')], max_length=10)),
                ('Role', models.CharField(max_length=20)),
                ('Billing_Date', models.DateField()),
                ('OnBoard_Date', models.DateField(default='2021-01-01')),
                ('Screening_Phase', models.CharField(choices=[('PENDING', 'PENDING'), ('WIP', 'WIP'), ('COMPLETE', 'COMPLETE')], max_length=20)),
                ('Final_status', models.CharField(choices=[('SELECTED', 'SELECTED'), ('REJECTED', 'REJECTED')], default='SELECTED', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PanelistSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Panel', models.CharField(max_length=100)),
                ('Available_from', models.DateTimeField()),
                ('Available_till', models.DateTimeField()),
            ],
        ),
    ]
