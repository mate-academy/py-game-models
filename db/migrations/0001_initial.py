# Generated by Django 4.0.2 on 2024-10-28 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guild',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('bonus', models.CharField(max_length=255, unique=True)),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='racess', to='db.race')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('email', models.CharField(max_length=255)),
                ('bio', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('guild', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='guilds', to='db.guild')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='races', to='db.race')),
            ],
        ),
    ]
