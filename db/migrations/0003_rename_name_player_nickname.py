# Generated by Django 4.0.2 on 2024-02-12 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_alter_player_race_alter_race_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='name',
            new_name='nickname',
        ),
    ]
