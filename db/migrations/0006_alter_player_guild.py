# Generated by Django 4.0.2 on 2022-10-10 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0005_alter_guild_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='guild',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='db.guild'),
        ),
    ]
