# Generated by Django 5.1.4 on 2024-12-09 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("menus", "0005_remove_footeritem_title_uk_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="footeritem",
            name="title_uk",
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="socialmedialink",
            name="url_uk",
            field=models.URLField(max_length=256, null=True),
        ),
    ]