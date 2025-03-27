from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("db", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="player",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
