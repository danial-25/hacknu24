# Generated by Django 4.2.2 on 2024-04-13 20:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reading_module", "0004_reading_puzzle"),
    ]

    operations = [
        migrations.AddField(
            model_name="reading_module",
            name="level",
            field=models.IntegerField(default=1),
        ),
    ]
