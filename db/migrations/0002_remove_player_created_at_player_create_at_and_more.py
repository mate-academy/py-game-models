# Generated by Django 4.0.2 on 2024-04-22 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='created_at',
        ),
        migrations.AddField(
            model_name='player',
            name='create_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
