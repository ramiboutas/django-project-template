# Generated by Django 5.1.3 on 2024-11-17 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("menus", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="navbarlink",
            old_name="site",
            new_name="sites",
        ),
    ]
