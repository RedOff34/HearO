# Generated by Django 4.2 on 2023-06-14 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Main", "0007_rename_writer_post_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="file",
            field=models.FileField(blank=True, upload_to=""),
        ),
    ]
