# Generated by Django 4.0.2 on 2023-06-06 16:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("db", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="guild",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
