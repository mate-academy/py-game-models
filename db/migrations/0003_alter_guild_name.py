# Generated by Django 4.0.2 on 2024-01-13 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_alter_guild_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guild',
            name='name',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]
