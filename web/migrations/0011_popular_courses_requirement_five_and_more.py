# Generated by Django 4.2.7 on 2023-11-24 14:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0010_popular_courses_topic_eight_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="popular_courses",
            name="requirement_five",
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="popular_courses",
            name="requirement_four",
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="popular_courses",
            name="requirement_one",
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="popular_courses",
            name="requirement_three",
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="popular_courses",
            name="requirement_two",
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
