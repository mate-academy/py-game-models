# Generated by Django 4.0.2 on 2023-09-07 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_alter_player_guild_alter_player_race_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='email',
            field=models.EmailField(max_length=255),
        ),
    ]
