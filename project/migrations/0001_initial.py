# Generated by Django 3.0.5 on 2020-04-06 22:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(default='Project name is unset', max_length=30, verbose_name='project title')),
                ('project_duration', models.IntegerField(default=0, verbose_name='estimated duration')),
                ('time_allocated_by_creator', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Allocated time')),
                ('needs', models.TextField(max_length=250)),
                ('description', models.TextField(max_length=250)),
                ('validity_state', models.BooleanField(default=False)),
            ],
        ),
    ]
