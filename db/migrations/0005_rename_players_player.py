# Generated by Django 4.0.2 on 2024-01-24 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0004_players'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Players',
            new_name='Player',
        ),
    ]
