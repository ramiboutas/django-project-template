# Generated by Django 5.0.2 on 2024-02-28 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("content", "0003_menulistitem_title_en_page_body_en_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="menulistitem",
            name="title_en_GB",
        ),
        migrations.RemoveField(
            model_name="page",
            name="body_en_GB",
        ),
        migrations.RemoveField(
            model_name="page",
            name="description_en_GB",
        ),
        migrations.RemoveField(
            model_name="page",
            name="slug_en_GB",
        ),
        migrations.RemoveField(
            model_name="page",
            name="title_en_GB",
        ),
        migrations.RemoveField(
            model_name="topic",
            name="name_en_GB",
        ),
        migrations.RemoveField(
            model_name="topic",
            name="slug_en_GB",
        ),
        migrations.AlterField(
            model_name="article",
            name="language",
            field=models.CharField(
                choices=[("en", "English"), ("es", "Spanish"), ("de", "German")],
                default="en",
                max_length=8,
            ),
        ),
        migrations.AlterField(
            model_name="home",
            name="language",
            field=models.CharField(
                choices=[("en", "English"), ("es", "Spanish"), ("de", "German")],
                default="en",
                max_length=8,
            ),
        ),
        migrations.AlterField(
            model_name="productpage",
            name="language",
            field=models.CharField(
                choices=[("en", "English"), ("es", "Spanish"), ("de", "German")],
                default="en",
                max_length=8,
            ),
        ),
    ]
