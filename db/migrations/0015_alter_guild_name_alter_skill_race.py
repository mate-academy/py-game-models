# Generated by Django 4.0.2 on 2025-01-09 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0014_alter_guild_description_alter_guild_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guild',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='db.race'),
        ),
    ]
