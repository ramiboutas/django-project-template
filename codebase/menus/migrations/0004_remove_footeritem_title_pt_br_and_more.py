# Generated by Django 5.1.4 on 2024-12-09 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("menus", "0003_remove_footeritem_title_eo_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="footeritem",
            name="title_pt_br",
        ),
        migrations.RemoveField(
            model_name="socialmedialink",
            name="url_pt_br",
        ),
    ]