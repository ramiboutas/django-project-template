# Generated by Django 4.2.5 on 2023-09-13 20:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("jobs", "0003_alter_profile_actual_position_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rockenjob",
            name="vacancy_url",
            field=models.CharField(max_length=1024),
        ),
    ]