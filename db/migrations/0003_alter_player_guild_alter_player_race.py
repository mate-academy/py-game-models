# Generated by Django 4.0.2 on 2024-04-22 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_player_guild_alter_guild_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='guild',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='players', to='db.guild'),
        ),
        migrations.AlterField(
            model_name='player',
            name='race',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='players', to='db.race'),
        ),
    ]
