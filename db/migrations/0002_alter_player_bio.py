# Generated by Django 4.0.2 on 2023-11-27 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='bio',
            field=models.CharField(max_length=255),
        ),
    ]
