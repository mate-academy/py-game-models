# Generated by Django 4.0.2 on 2023-10-23 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_rename_guild_id_player_guild_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='guild',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='db.guild'),
        ),
    ]