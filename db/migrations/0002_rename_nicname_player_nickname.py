# Generated by Django 4.0.2 on 2024-07-12 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='nicname',
            new_name='nickname',
        ),
    ]
