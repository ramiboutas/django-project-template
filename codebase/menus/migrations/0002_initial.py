# Generated by Django 5.1.4 on 2024-12-19 19:34

import auto_prefetch
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("links", "0002_initial"),
        ("menus", "0001_initial"),
        ("sites", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="footeritem",
            name="sites",
            field=models.ManyToManyField(to="sites.site"),
        ),
        migrations.AddField(
            model_name="footerlink",
            name="footer_item",
            field=auto_prefetch.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="menus.footeritem",
            ),
        ),
        migrations.AddField(
            model_name="footerlink",
            name="link",
            field=auto_prefetch.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="links.link"
            ),
        ),
        migrations.AddField(
            model_name="footerlink",
            name="sites",
            field=models.ManyToManyField(to="sites.site"),
        ),
        migrations.AddField(
            model_name="navbarlink",
            name="link",
            field=auto_prefetch.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="links.link"
            ),
        ),
        migrations.AddField(
            model_name="navbarlink",
            name="sites",
            field=models.ManyToManyField(to="sites.site"),
        ),
        migrations.AddField(
            model_name="socialmedialink",
            name="sites",
            field=models.ManyToManyField(to="sites.site"),
        ),
    ]
