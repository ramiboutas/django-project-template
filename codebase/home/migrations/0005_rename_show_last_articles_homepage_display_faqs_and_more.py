# Generated by Django 5.1.3 on 2024-11-21 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_homepage_benefits_title_de_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="homepage",
            old_name="show_last_articles",
            new_name="display_faqs",
        ),
        migrations.AddField(
            model_name="homepage",
            name="display_last_articles",
            field=models.BooleanField(default=False),
        ),
    ]
