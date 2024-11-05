# Generated by Django 5.1.3 on 2024-11-05 21:31

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0018_rename_siteattrs_website"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="website",
            name="brand_name",
        ),
        migrations.AddField(
            model_name="website",
            name="change_theme_light_in_footer",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="website",
            name="change_theme_light_in_navbar",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="website",
            name="default_page_description",
            field=models.TextField(default="Hello", max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="website",
            name="default_page_keywords",
            field=models.CharField(default=django.utils.timezone.now, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="website",
            name="default_page_title",
            field=models.CharField(default="DEfault page title", max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="website",
            name="emoji",
            field=models.CharField(default="🍊", max_length=8),
        ),
        migrations.AddField(
            model_name="website",
            name="emoji_in_brand",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="website",
            name="footer_links_separator",
            field=models.CharField(default="🍊", max_length=8),
        ),
        migrations.AlterField(
            model_name="website",
            name="title",
            field=models.TextField(default=""),
        ),
    ]
