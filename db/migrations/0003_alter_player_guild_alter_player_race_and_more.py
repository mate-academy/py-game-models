# Generated by Django 4.0.2 on 2023-06-29 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_alter_player_guild'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='guild',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='db.guild'),
        ),
        migrations.AlterField(
            model_name='player',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.race'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.race'),
        ),
    ]
