# Generated by Django 4.2 on 2023-06-12 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Comment",
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
                ("comment_id", models.PositiveIntegerField()),
                ("user_id", models.CharField(max_length=20)),
                ("content", models.TextField(max_length=100)),
                ("post_id", models.CharField(max_length=50)),
                ("date", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="History",
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
                ("hist_id", models.PositiveIntegerField()),
                ("user_id", models.CharField(max_length=20)),
                ("date", models.DateTimeField()),
                ("location", models.CharField(max_length=50)),
                ("file", models.FileField(upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="Post",
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
                ("post_id", models.PositiveIntegerField()),
                ("user_id", models.CharField(max_length=20)),
                ("content", models.CharField(max_length=300)),
                ("date", models.DateTimeField()),
                ("file", models.FileField(upload_to="")),
            ],
        ),
    ]
