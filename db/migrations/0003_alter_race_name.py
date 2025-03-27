# Generated by Django 4.0.2 on 2024-09-19 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_alter_race_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='race',
            name='name',
            field=models.CharField(choices=[('elf', 'Elf Race'), ('dwarf', 'Dwarf Race'), ('human', 'Human Race'), ('ork', 'Ork Race')], default='Unknown', max_length=255, unique=True),
        ),
    ]
