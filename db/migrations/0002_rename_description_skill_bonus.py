# Generated by Django 4.0.2 on 2024-02-06 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='description',
            new_name='bonus',
        ),
    ]
