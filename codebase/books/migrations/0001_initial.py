# Generated by Django 5.1.4 on 2024-12-19 21:23

import auto_prefetch
import codebase.base.utils.mixins
import codebase.books.models
import django.db.models.deletion
import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("sites", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("name", models.CharField(max_length=64, unique=True)),
                ("sites", models.ManyToManyField(to="sites.site")),
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
        migrations.CreateModel(
            name="Chapter",
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
                ("title", models.CharField(editable=False, max_length=256)),
                ("slug", models.SlugField(editable=False, max_length=128, unique=True)),
                ("folder_name", models.CharField(editable=False, max_length=128)),
                ("subfolder_name", models.CharField(editable=False, max_length=256)),
                ("body", models.TextField(editable=False)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("can_be_shown_in_home", models.BooleanField(default=True)),
                (
                    "book",
                    auto_prefetch.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="books.book"
                    ),
                ),
            ],
            options={
                "ordering": ["-created_on"],
                "abstract": False,
                "base_manager_name": "prefetch_manager",
                "unique_together": {("folder_name", "subfolder_name")},
            },
            bases=(models.Model, codebase.base.utils.mixins.PageMixin),
            managers=[
                ("objects", django.db.models.manager.Manager()),
                ("prefetch_manager", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="ChapterFile",
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
                        upload_to=codebase.books.models.get_chapter_file_path
                    ),
                ),
                (
                    "chapter",
                    auto_prefetch.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="books.chapter"
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
