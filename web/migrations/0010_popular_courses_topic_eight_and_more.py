# Generated by Django 4.2.7 on 2023-11-24 14:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0009_popular_courses_first_content_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="popular_courses",
            name="topic_eight",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="popular_courses",
            name="topic_five",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="popular_courses",
            name="topic_four",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="popular_courses",
            name="topic_one",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="popular_courses",
            name="topic_seven",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="popular_courses",
            name="topic_six",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="popular_courses",
            name="topic_three",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="popular_courses",
            name="topic_two",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
