# Generated by Django 4.2 on 2023-06-30 19:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_danger"),
    ]

    operations = [
        migrations.RenameField(
            model_name="danger",
            old_name="user",
            new_name="user_id",
        ),
        migrations.AddField(
            model_name="danger",
            name="user_name",
            field=models.CharField(default=django.utils.timezone.now, max_length=5),
            preserve_default=False,
        ),
    ]
