# Generated by Django 5.0.6 on 2024-07-04 07:36

import datetime
import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('avatar', models.ImageField(upload_to='images/avatars/', verbose_name='Avatar')),
                ('number', models.CharField(max_length=20, unique=True, verbose_name='Number')),
                ('birth_date', models.DateField(blank=True, default=datetime.date(2000, 1, 1), verbose_name='Birth date')),
                ('first_name', models.CharField(max_length=50, verbose_name='Surname')),
                ('last_name', models.CharField(max_length=50, verbose_name='Name')),
                ('patronymic', models.CharField(default=None, max_length=50, null=True, verbose_name='Отчество')),
                ('email', models.EmailField(blank=True, max_length=254, unique=True, verbose_name='email')),
                ('password', models.CharField(max_length=50, verbose_name='password')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Time')),
                ('user_type', models.CharField(choices=[('doctor', 'Doctor'), ('patient', 'Patient'), ('admin', 'Admin')], default='patient', max_length=20, verbose_name='Type of User')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='management.user')),
                ('Bachelor <django.db.models.query_utils.DeferredAttribute object at 0x0000027045BE7070>', models.ImageField(upload_to='images/educations/', verbose_name='Bachelory documents')),
                ('Master <django.db.models.query_utils.DeferredAttribute object at 0x0000027045BE7070>', models.ImageField(null=True, upload_to='images/educations/', verbose_name='Master documents')),
                ('experience', models.IntegerField(verbose_name='experience')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('schedule', models.CharField(max_length=20, verbose_name='Schedule time')),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Rating of doctor')),
                ('is_verified', models.BooleanField(default=None, verbose_name='Is real doc?')),
            ],
            options={
                'verbose_name': 'doctor',
                'verbose_name_plural': 'doctors',
            },
            bases=('management.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='management.user')),
            ],
            options={
                'verbose_name': 'patient',
                'verbose_name_plural': 'patients',
            },
            bases=('management.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
