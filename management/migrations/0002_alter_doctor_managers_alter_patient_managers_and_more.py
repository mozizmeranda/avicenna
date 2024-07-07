# Generated by Django 5.0.6 on 2024-07-05 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='doctor',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='patient',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='Bachelor <django.db.models.query_utils.DeferredAttribute object at 0x0000027045BE7070>',
            new_name='Bachelor <django.db.models.query_utils.DeferredAttribute object at 0x0000011E16CF4070>',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='Master <django.db.models.query_utils.DeferredAttribute object at 0x0000027045BE7070>',
            new_name='Master <django.db.models.query_utils.DeferredAttribute object at 0x0000011E16CF4070>',
        ),
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
    ]
