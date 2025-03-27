# Generated by Django 4.0.2 on 2023-03-02 20:17

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
                ('bonus', models.CharField(max_length=255, verbose_name='describes what kind of bonus players can get from it.')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.race')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=255)),
                ('bio', models.CharField(max_length=255, verbose_name='stores a short description provided by a user about himself/herself')),
                ('created_at', models.DateField(auto_now=True)),
                ('guild', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='guilds', to='db.guild')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='races', to='db.race')),
            ],
        ),
    ]
