# Generated by Django 4.1.6 on 2023-02-21 03:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0003_externalfilesnippetassociateddocument"),
    ]

    operations = [
        migrations.AddField(
            model_name="document",
            name="name",
            field=models.TextField(default="vazio"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="document",
            name="path",
            field=models.TextField(default="nada"),
            preserve_default=False,
        ),
    ]