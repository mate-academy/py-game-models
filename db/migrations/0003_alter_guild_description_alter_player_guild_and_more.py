# Generated by Django 4.0.2 on 2022-10-06 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_rename_rase_skill_race'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guild',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='guild',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='db.guild'),
        ),
        migrations.AlterField(
            model_name='race',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
