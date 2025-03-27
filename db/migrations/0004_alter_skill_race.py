# Generated by Django 4.0.2 on 2024-08-26 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_player_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skill_set', to='db.race'),
        ),
    ]
