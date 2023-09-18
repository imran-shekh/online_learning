# Generated by Django 4.2.3 on 2023-08-21 07:20

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course_Details",
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
                (
                    "course_name",
                    models.CharField(default="", max_length=100, null=True),
                ),
                ("slug", models.CharField(default="", max_length=100, null=True)),
                ("desc", models.CharField(default="", max_length=100, null=True)),
                ("price", models.IntegerField(default=1, null=True)),
                ("discount", models.IntegerField(default=1, null=True)),
                ("course_img", models.ImageField(upload_to="static/images/")),
                ("resource", models.FileField(upload_to="resources/course")),
                ("duration", models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name="Signup",
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
                ("first_name", models.CharField(default="", max_length=100, null=True)),
                ("last_name", models.CharField(default="", max_length=100, null=True)),
                ("email", models.CharField(default="", max_length=100, null=True)),
                ("password", models.CharField(default="", max_length=255, null=True)),
                ("age", models.IntegerField(null=True)),
                ("mobile", models.BigIntegerField(null=True)),
                ("gender", models.CharField(default="", max_length=100, null=True)),
            ],
        ),
    ]
