# Generated by Django 4.0.2 on 2022-09-07 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_alter_guild_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guild',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
