# Generated by Django 4.2.7 on 2023-11-24 13:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0007_popular_courses_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="popular_courses",
            name="slug",
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
