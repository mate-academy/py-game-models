# Generated by Django 4.0.2 on 2025-01-09 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_alter_skill_race'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='description',
            new_name='bonus',
        ),
    ]
