# Generated by Django 5.1.3 on 2024-11-23 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0008_rename_sites_userhomepage_site"),
        ("sites", "0002_alter_domain_unique"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userhomepage",
            name="site",
        ),
        migrations.AddField(
            model_name="userhomepage",
            name="sites",
            field=models.ManyToManyField(to="sites.site"),
        ),
    ]