# Generated by Django 5.0.3 on 2024-03-29 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("content", "0012_topic_listing_tag_alter_listingproduct_public"),
    ]

    operations = [
        migrations.AlterField(
            model_name="topic",
            name="slug",
            field=models.SlugField(max_length=32),
        ),
        migrations.AlterField(
            model_name="topic",
            name="slug_de",
            field=models.SlugField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name="topic",
            name="slug_en",
            field=models.SlugField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name="topic",
            name="slug_es",
            field=models.SlugField(max_length=32, null=True),
        ),
    ]