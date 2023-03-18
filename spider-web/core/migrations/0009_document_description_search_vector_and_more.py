# Generated by Django 4.1.6 on 2023-03-18 22:52

import django.contrib.postgres.indexes
import django.contrib.postgres.search
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0008_document_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="document",
            name="description_search_vector",
            field=django.contrib.postgres.search.SearchVectorField(null=True),
        ),
        migrations.AddIndex(
            model_name="document",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["description_search_vector"], name="core_docume_descrip_631438_gin"
            ),
        ),
    ]
