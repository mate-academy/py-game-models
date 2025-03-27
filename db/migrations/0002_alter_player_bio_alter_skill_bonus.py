# Generated by Django 4.0.2 on 2023-09-10 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='bio',
            field=models.CharField(max_length=255, verbose_name='Bio stores a short description provided by a user about himself/herself.'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='bonus',
            field=models.CharField(max_length=255, verbose_name='Bonus describes what kind of bonus players can get from skill.'),
        ),
    ]
