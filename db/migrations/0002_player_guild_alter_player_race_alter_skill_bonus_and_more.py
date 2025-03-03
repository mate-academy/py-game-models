# Generated by Django 4.0.2 on 2023-06-21 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("db", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="player",
            name="guild",
            field=models.ForeignKey(
                default=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="db.guild",
            ),
        ),
        migrations.AlterField(
            model_name="player",
            name="race",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="db.race"
            ),
        ),
        migrations.AlterField(
            model_name="skill",
            name="bonus",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="skill",
            name="race",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="db.race"
            ),
        ),
    ]
