# Generated by Django 4.1.3 on 2022-12-05 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0002_alter_desires_model_d1_alter_desires_model_d1t1_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="report",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="teaching",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="vip",
            field=models.BooleanField(default=False, null=True),
        ),
    ]
