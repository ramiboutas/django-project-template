# Generated by Django 5.1.4 on 2024-12-19 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0001_initial"),
        ("sites", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="site",
            name="books",
            field=models.ManyToManyField(to="books.book"),
        ),
    ]
