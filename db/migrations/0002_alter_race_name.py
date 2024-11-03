# Generated by Django 4.0.2 on 2024-11-03 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='race',
            name='name',
            field=models.CharField(choices=[('Elf', 'Elf race'), ('Dwarf', 'Dwarf race'), ('Human', 'Human race'), ('Ork', 'Ork race')], max_length=255, unique=True),
        ),
    ]
