# Generated by Django 4.0.2 on 2024-06-07 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0005_alter_player_guild_alter_race_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='guild',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='players', to='db.guild'),
        ),
    ]
