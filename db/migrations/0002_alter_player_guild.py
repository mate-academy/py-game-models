# Generated by Django 4.0.2 on 2024-05-01 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='guild',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='db.guild'),
        ),
    ]
