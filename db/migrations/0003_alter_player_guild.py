# Generated by Django 4.0.2 on 2025-02-05 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_alter_player_guild'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='guild',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='db.guild'),
        ),
    ]
