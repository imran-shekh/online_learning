# Generated by Django 4.2.3 on 2023-08-23 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("onlearn_new", "0002_videos"),
    ]

    operations = [
        migrations.AddField(
            model_name="videos",
            name="video_belong",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="onlearn_new.course_details",
            ),
        ),
        migrations.AddField(
            model_name="videos",
            name="video_seq",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
