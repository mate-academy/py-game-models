# Generated by Django 4.0.2 on 2024-04-03 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_alter_guild_description_alter_player_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='race',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
