# Generated by Django 5.1.3 on 2024-11-18 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("menus", "0004_alter_footerlink_link"),
    ]

    operations = [
        migrations.RenameField(
            model_name="footerlink",
            old_name="site",
            new_name="sites",
        ),
    ]