# Generated by Django 4.0.2 on 2024-07-21 11:49

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
                ('name', models.CharField(max_length=255)),
                ('bonus', models.CharField(max_length=255)),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skill', to='db.race')),
            ],
        ),
        migrations.CreateModel(
            name='Prayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=255)),
                ('bio', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('guild', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='prayer', to='db.guild')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prayer', to='db.race')),
            ],
        ),
    ]
