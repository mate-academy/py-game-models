# Generated by Django 4.0.2 on 2025-02-24 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_alter_guild_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='bio',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='skill',
            name='bonus',
            field=models.CharField(max_length=255),
        ),
    ]
