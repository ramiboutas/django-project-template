# Generated by Django 5.1.2 on 2024-10-19 14:31

import auto_prefetch
import django.db.models.deletion
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0002_alter_article_body_alter_article_body_de_and_more"),
        ("base", "0001_initial"),
        ("pages", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="pagelink",
            name="article",
            field=auto_prefetch.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="articles.article",
            ),
        ),
        migrations.AddField(
            model_name="pagelink",
            name="page",
            field=auto_prefetch.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="pages.page",
            ),
        ),
    ]
