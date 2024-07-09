# Generated by Django 4.0.2 on 2024-07-09 01:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_rename_player_model_playermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=255)),
                ('bio', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('guild', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='db.guild')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.race')),
            ],
        ),
        migrations.DeleteModel(
            name='PlayerModel',
        ),
    ]
