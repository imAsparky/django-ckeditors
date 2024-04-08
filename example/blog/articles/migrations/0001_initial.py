# Generated by Django 5.0.4 on 2024-04-08 23:41

import django.db.models.deletion
from django.db import migrations, models

import django_ckeditors.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=200, null=True, verbose_name="Title"),
                ),
                ("text", django_ckeditors.fields.CKEditorsField(verbose_name="Text")),
                (
                    "text2",
                    django_ckeditors.fields.CKEditorsField(
                        blank=True, null=True, verbose_name="Text 2",
                    ),
                ),
            ],
            options={
                "verbose_name": "Article",
                "verbose_name_plural": "Articles",
            },
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("author", models.CharField(max_length=250)),
                ("text", django_ckeditors.fields.CKEditorsField(verbose_name="Text")),
                (
                    "article",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="articles.article",
                    ),
                ),
            ],
            options={
                "verbose_name": "Comment",
                "verbose_name_plural": "Comments",
            },
        ),
    ]
