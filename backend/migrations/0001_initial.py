# Generated by Django 4.2 on 2023-04-13 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opprettet', models.DateTimeField(auto_now_add=True)),
                ('oppgavetekst', models.CharField(max_length=200)),
                ('frist', models.DateTimeField(blank=True, null=True)),
                ('ferdig', models.BooleanField(default=False)),
            ],
        ),
    ]
