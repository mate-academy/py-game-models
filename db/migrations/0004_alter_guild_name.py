# Generated by Django 4.0.2 on 2025-02-07 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_alter_guild_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guild',
            name='name',
            field=models.CharField(default='', max_length=255, unique=True),
        ),
    ]
