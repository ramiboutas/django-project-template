# Generated by Django 5.1.3 on 2024-11-05 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0017_alter_siteattrs_options"),
        ("sites", "0002_alter_domain_unique"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="SiteAttrs",
            new_name="Website",
        ),
    ]
