# Generated by Django 5.1.3 on 2024-11-21 20:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0006_userhomepage_allow_field_translation_and_more"),
        ("sites", "0002_alter_domain_unique"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userhomepage",
            name="sites",
        ),
        migrations.AddField(
            model_name="userhomepage",
            name="sites",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="sites.site"
            ),
            preserve_default=False,
        ),
    ]