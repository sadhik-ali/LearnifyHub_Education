# Generated by Django 4.2.7 on 2023-11-24 14:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0008_alter_popular_courses_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="popular_courses",
            name="first_content",
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="popular_courses",
            name="second_content",
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
