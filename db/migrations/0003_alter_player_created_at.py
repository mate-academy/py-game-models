# Generated by Django 4.0.2 on 2023-09-07 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_alter_skill_race'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
