# Generated by Django 4.0.2 on 2023-10-16 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_guild_skill_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]