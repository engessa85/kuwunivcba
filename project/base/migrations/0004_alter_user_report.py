# Generated by Django 4.1.3 on 2022-12-05 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0003_user_report_user_teaching_user_vip"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="report",
            field=models.CharField(max_length=10, null=True),
        ),
    ]