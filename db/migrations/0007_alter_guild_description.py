# Generated by Django 4.0.2 on 2025-02-26 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0006_alter_guild_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guild',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
