# Generated by Django 4.1.3 on 2022-11-26 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_alter_post_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(default="", upload_to="blog/images/"),
        ),
    ]
