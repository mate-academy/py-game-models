# Generated by Django 4.0.2 on 2023-04-02 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_alter_player_guild_alter_skill_race'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='player_race', to='db.race'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skill_set', to='db.race'),
        ),
    ]
