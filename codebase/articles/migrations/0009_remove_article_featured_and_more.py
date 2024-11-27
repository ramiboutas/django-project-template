# Generated by Django 5.1.3 on 2024-11-27 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0008_remove_article_submodule_folder"),
        ("sites", "0002_alter_domain_unique"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="article",
            name="featured",
        ),
        migrations.RemoveField(
            model_name="articlefile",
            name="parent_page",
        ),
        migrations.AddField(
            model_name="articlesfolder",
            name="sites",
            field=models.ManyToManyField(to="sites.site"),
        ),
    ]