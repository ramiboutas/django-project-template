# Generated by Django 5.1.3 on 2024-11-05 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0020_remove_website_footer_links_separator"),
        ("menus", "0020_alter_footeritem_show_type_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="footeritem",
            name="website",
            field=models.ManyToManyField(to="base.website"),
        ),
        migrations.AddField(
            model_name="footerlink",
            name="website",
            field=models.ManyToManyField(to="base.website"),
        ),
        migrations.AddField(
            model_name="navbarlink",
            name="website",
            field=models.ManyToManyField(to="base.website"),
        ),
        migrations.AddField(
            model_name="socialmedialink",
            name="website",
            field=models.ManyToManyField(to="base.website"),
        ),
    ]
