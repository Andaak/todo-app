# Generated by Django 4.2 on 2023-04-10 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_todo_frist_todo_oprettet'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='dato_fullført',
            field=models.DateField(blank=True, null=True),
        ),
    ]
