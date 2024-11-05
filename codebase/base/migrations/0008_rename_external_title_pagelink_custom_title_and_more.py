# Generated by Django 5.1.2 on 2024-10-31 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0007_alter_pagelink_options_pagelink_order"),
    ]

    operations = [
        migrations.RenameField(
            model_name="pagelink",
            old_name="external_title",
            new_name="custom_title",
        ),
        migrations.RenameField(
            model_name="pagelink",
            old_name="external_title_de",
            new_name="custom_title_de",
        ),
        migrations.RenameField(
            model_name="pagelink",
            old_name="external_title_en",
            new_name="custom_title_en",
        ),
        migrations.RenameField(
            model_name="pagelink",
            old_name="external_title_es",
            new_name="custom_title_es",
        ),
    ]