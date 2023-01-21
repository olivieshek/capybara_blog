# Generated by Django 4.1.3 on 2023-01-21 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_modelcategory_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="modelcategory",
            name="slug",
        ),
        migrations.AddField(
            model_name="post",
            name="slug",
            field=models.SlugField(null=True, unique=True),
        ),
    ]