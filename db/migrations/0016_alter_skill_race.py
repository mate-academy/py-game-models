# Generated by Django 4.0.2 on 2025-01-09 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0015_alter_guild_name_alter_skill_race'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skill_set', to='db.race'),
        ),
    ]
