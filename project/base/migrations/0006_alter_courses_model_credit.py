# Generated by Django 4.1.3 on 2022-12-09 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0005_courses_model_credit"),
    ]

    operations = [
        migrations.AlterField(
            model_name="courses_model",
            name="credit",
            field=models.PositiveIntegerField(null=True),
        ),
    ]
