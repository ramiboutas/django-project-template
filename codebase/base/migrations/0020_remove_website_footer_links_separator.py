# Generated by Django 5.1.3 on 2024-11-05 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0019_remove_website_brand_name_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="website",
            name="footer_links_separator",
        ),
    ]