# Generated by Django 5.1.3 on 2024-11-17 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0002_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="articlesfolder",
            name="is_premium",
        ),
        migrations.AddField(
            model_name="article",
            name="is_premium",
            field=models.BooleanField(default=False),
        ),
    ]