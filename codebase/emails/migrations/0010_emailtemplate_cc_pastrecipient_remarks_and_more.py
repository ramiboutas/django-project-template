# Generated by Django 5.0.4 on 2024-05-25 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("emails", "0009_remove_pastrecipient_addresses_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="emailtemplate",
            name="cc",
            field=models.EmailField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="pastrecipient",
            name="remarks",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="recipient",
            name="remarks",
            field=models.TextField(blank=True, null=True),
        ),
    ]
