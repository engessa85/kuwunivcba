# Generated by Django 4.1.3 on 2022-12-09 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0004_alter_user_report"),
    ]

    operations = [
        migrations.AddField(
            model_name="courses_model",
            name="credit",
            field=models.IntegerField(null=True),
        ),
    ]
