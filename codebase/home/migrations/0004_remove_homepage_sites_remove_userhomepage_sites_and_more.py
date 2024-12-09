# Generated by Django 5.1.3 on 2024-12-08 21:41

import auto_prefetch
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_initial"),
        ("sites", "0003_domain_is_main"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="homepage",
            name="sites",
        ),
        migrations.RemoveField(
            model_name="userhomepage",
            name="sites",
        ),
        migrations.AddField(
            model_name="benefitssection",
            name="allow_translation",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="benefitssection",
            name="override_translated_fields",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="homepage",
            name="site",
            field=auto_prefetch.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="sites.site"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="solutionsection",
            name="allow_translation",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="solutionsection",
            name="override_translated_fields",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="stepaction",
            name="allow_translation",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="stepaction",
            name="override_translated_fields",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="userhomepage",
            name="site",
            field=auto_prefetch.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="sites.site"
            ),
            preserve_default=False,
        ),
    ]
