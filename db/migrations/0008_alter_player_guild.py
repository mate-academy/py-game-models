# Generated by Django 4.0.2 on 2024-06-07 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0007_alter_player_guild'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='guild',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='players', to='db.guild'),
        ),
    ]
