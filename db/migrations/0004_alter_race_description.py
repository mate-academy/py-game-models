# Generated by Django 4.0.2 on 2023-09-11 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_alter_player_race'),
    ]

    operations = [
        migrations.AlterField(
            model_name='race',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
