# Generated by Django 4.0.2 on 2022-12-12 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_alter_player_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='name',
            new_name='nickname',
        ),
    ]
