# Generated by Django 4.0.2 on 2024-03-20 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_alter_race_description_alter_race_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='guild',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.guild'),
        ),
        migrations.AlterField(
            model_name='player',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.race'),
        ),
        migrations.AlterField(
            model_name='race',
            name='name',
            field=models.CharField(choices=[('Elf', 'The magic race'), ('Dwarf', 'DWARF'), ('Human', 'Human race'), ('Ork', 'ORK')], max_length=255),
        ),
        migrations.AlterField(
            model_name='skill',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.race'),
        ),
    ]
