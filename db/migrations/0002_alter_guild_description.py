# Generated by Django 4.0.2 on 2024-01-15 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guild',
            name='description',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
