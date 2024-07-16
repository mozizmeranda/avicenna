# Generated by Django 5.0.6 on 2024-07-12 08:07

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='patient',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='doctor',
            name='master_document',
            field=models.ImageField(blank=True, null=True, upload_to='images/educations/', verbose_name='Master documents'),
        ),
    ]
