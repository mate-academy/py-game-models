# Generated by Django 5.0.6 on 2024-05-31 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_alter_player_created_at_alter_player_guilg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='guilg',
            new_name='guild',
        ),
    ]
