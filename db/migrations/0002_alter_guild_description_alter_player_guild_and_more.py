# Generated by Django 4.0.2 on 2025-02-10 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
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
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='members', to='db.guild'),
        ),
        migrations.AlterField(
            model_name='player',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='db.race'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='db.race'),
        ),
    ]
