# Generated by Django 4.1.6 on 2023-02-24 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("golf", "0010_change_reverse_relationships"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="like",
            unique_together={("user", "content_type", "object_id")},
        ),
    ]
