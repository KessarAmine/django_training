# Generated by Django 4.2.4 on 2023-08-21 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Users",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("birthday", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Comments",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.CharField(max_length=50)),
                (
                    "author_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="comments_module.users",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Blog_posts",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("posted_at", models.DateField()),
                ("post_text", models.CharField(max_length=3000)),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="comments_module.users",
                    ),
                ),
            ],
        ),
    ]
