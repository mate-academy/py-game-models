# Generated by Django 4.0.2 on 2024-10-12 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0007_alter_player_email_alter_player_guild'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.race'),
        ),
    ]
