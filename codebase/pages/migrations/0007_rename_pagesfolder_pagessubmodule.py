# Generated by Django 5.1.3 on 2024-11-27 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "base",
            "0021_rename_default_page_description_extendedsite_page_description_and_more",
        ),
        ("pages", "0006_remove_page_submodule_folder_page_sites"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="PagesFolder",
            new_name="PagesSubmodule",
        ),
    ]