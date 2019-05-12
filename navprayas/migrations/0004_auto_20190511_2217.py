# Generated by Django 2.2 on 2019-05-11 22:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navprayas', '0003_auto_20190511_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mtse',
            name='class_study',
        ),
        migrations.AlterField(
            model_name='mtse',
            name='gender',
            field=models.CharField(blank=True, choices=[('Female1', 'Female'), ('Male1', 'Male')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='mtse',
            name='pin',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(100000), django.core.validators.MaxValueValidator(999999)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('Female1', 'Female'), ('Male1', 'Male')], default='Male', max_length=50),
        ),
    ]
