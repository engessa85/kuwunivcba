# Generated by Django 4.1.3 on 2022-12-09 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0008_alter_days_model_title_alter_dt_model_time_value"),
    ]

    operations = [
        migrations.AlterField(
            model_name="courses_model",
            name="number",
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="courses_model",
            name="title",
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
