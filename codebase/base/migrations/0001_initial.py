# Generated by Django 5.1.2 on 2024-10-14 13:59

import auto_prefetch
import django.db.models.deletion
import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FooterItem",
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
                ("title", models.CharField(max_length=64)),
                ("title_en", models.CharField(max_length=64, null=True)),
                ("title_de", models.CharField(max_length=64, null=True)),
                ("title_es", models.CharField(max_length=64, null=True)),
                ("order", models.IntegerField(default=0)),
            ],
            options={
                "ordering": ("order",),
                "abstract": False,
                "base_manager_name": "prefetch_manager",
            },
            managers=[
                ("objects", django.db.models.manager.Manager()),
                ("prefetch_manager", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="NavbarItem",
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
                ("title", models.CharField(max_length=64)),
                ("title_en", models.CharField(max_length=64, null=True)),
                ("title_de", models.CharField(max_length=64, null=True)),
                ("title_es", models.CharField(max_length=64, null=True)),
                (
                    "location",
                    models.CharField(
                        choices=[("left", "Left"), ("right", "Right")],
                        default="right",
                        max_length=8,
                    ),
                ),
                ("order", models.IntegerField(default=0)),
            ],
            options={
                "ordering": ("order",),
                "abstract": False,
                "base_manager_name": "prefetch_manager",
            },
            managers=[
                ("objects", django.db.models.manager.Manager()),
                ("prefetch_manager", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="PageLink",
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
                (
                    "custom_title",
                    models.CharField(blank=True, max_length=128, null=True),
                ),
                (
                    "custom_title_en",
                    models.CharField(blank=True, max_length=128, null=True),
                ),
                (
                    "custom_title_de",
                    models.CharField(blank=True, max_length=128, null=True),
                ),
                (
                    "custom_title_es",
                    models.CharField(blank=True, max_length=128, null=True),
                ),
                (
                    "external_url",
                    models.URLField(blank=True, max_length=128, null=True),
                ),
                ("target_blank", models.BooleanField(default=False)),
                (
                    "footer_item",
                    auto_prefetch.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="base.footeritem",
                    ),
                ),
                (
                    "navbar_item",
                    auto_prefetch.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="base.navbaritem",
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
