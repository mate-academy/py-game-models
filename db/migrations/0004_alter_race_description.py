# Generated by Django 4.1 on 2024-08-29 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("db", "0003_alter_skill_race"),
    ]

    operations = [
        migrations.AlterField(
            model_name="race",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
