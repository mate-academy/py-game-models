# Generated by Django 4.0.2 on 2022-09-09 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_skill_race'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='race',
            field=models.ForeignKey(default=[], on_delete=django.db.models.deletion.CASCADE, to='db.race'),
        ),
    ]
