# Generated by Django 5.1.2 on 2024-10-18 09:23

import auto_prefetch
import codebase.articles.models
import django.db.models.deletion
import django.db.models.manager
import markdownx.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=256)),
                ("title_en", models.CharField(max_length=256, null=True)),
                ("title_de", models.CharField(max_length=256, null=True)),
                ("title_es", models.CharField(max_length=256, null=True)),
                ("slug", models.SlugField(editable=False, max_length=128, unique=True)),
                (
                    "slug_en",
                    models.SlugField(
                        editable=False, max_length=128, null=True, unique=True
                    ),
                ),
                (
                    "slug_de",
                    models.SlugField(
                        editable=False, max_length=128, null=True, unique=True
                    ),
                ),
                (
                    "slug_es",
                    models.SlugField(
                        editable=False, max_length=128, null=True, unique=True
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("folder", models.CharField(max_length=128)),
                ("subfolder", models.CharField(max_length=256)),
                ("body", markdownx.models.MarkdownxField()),
                ("body_en", markdownx.models.MarkdownxField(null=True)),
                ("body_de", markdownx.models.MarkdownxField(null=True)),
                ("body_es", markdownx.models.MarkdownxField(null=True)),
            ],
            options={
                "abstract": False,
                "base_manager_name": "prefetch_manager",
                "unique_together": {("folder", "subfolder")},
            },
            managers=[
                ("objects", django.db.models.manager.Manager()),
                ("prefetch_manager", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="ArticleFile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                (
                    "file",
                    models.FileField(
                        upload_to=codebase.articles.models.upload_article_file
                    ),
                ),
                (
                    "article",
                    auto_prefetch.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="articles.article",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "base_manager_name": "prefetch_manager",
            },
            managers=[
                ("objects", django.db.models.manager.Manager()),
                ("prefetch_manager", django.db.models.manager.Manager()),
            ],
        ),
    ]
