# Generated by Django 5.1.4 on 2024-12-15 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0008_alter_player_email_alter_player_race'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guild',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='email',
            field=models.EmailField(default='<EMAIL>', max_length=255),
        ),
    ]
