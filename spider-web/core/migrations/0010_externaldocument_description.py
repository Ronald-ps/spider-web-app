# Generated by Django 4.1.6 on 2023-03-18 23:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0009_document_description_search_vector_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="externaldocument",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
