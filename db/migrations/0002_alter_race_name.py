# Generated by Django 4.0.2 on 2022-10-20 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='race',
            name='name',
            field=models.CharField(choices=[('elf', 'ELf'), ('dwarf', 'Dwarf'), ('human', 'Human'), ('ork', 'Ork')], max_length=255, unique=True),
        ),
    ]
