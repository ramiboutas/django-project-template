# Generated by Django 5.1.4 on 2024-12-09 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("faqs", "0005_remove_faq_answer_uk_remove_faq_question_uk"),
    ]

    operations = [
        migrations.AddField(
            model_name="faq",
            name="answer_uk",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="question_uk",
            field=models.CharField(max_length=256, null=True),
        ),
    ]
