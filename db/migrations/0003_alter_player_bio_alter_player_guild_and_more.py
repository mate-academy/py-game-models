# Generated by Django 4.0.2 on 2024-07-14 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_rename_nicname_player_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='bio',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='player',
            name='guild',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='db.guild'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='bonus',
            field=models.CharField(max_length=255),
        ),
    ]
