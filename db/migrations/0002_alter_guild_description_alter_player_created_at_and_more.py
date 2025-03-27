# Generated by Django 4.0.2 on 2023-08-17 14:45

from django.db import migrations, models


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
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
