# Generated by Django 5.0.3 on 2024-03-16 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("content", "0007_remove_productpagefeature_product_page_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="listingproduct",
            name="public",
            field=models.BooleanField(default=True),
        ),
    ]
