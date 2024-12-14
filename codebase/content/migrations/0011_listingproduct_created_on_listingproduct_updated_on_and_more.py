# Generated by Django 5.0.3 on 2024-03-17 12:45

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("content", "0010_remove_listingproduct_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="listingproduct",
            name="created_on",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="listingproduct",
            name="updated_on",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.DeleteModel(
            name="ArticlesRedirect",
        ),
    ]