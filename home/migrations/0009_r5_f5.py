# Generated by Django 2.2.9 on 2020-01-09 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0008_auto_20200109_1537"),
    ]

    operations = [
        migrations.AddField(
            model_name="r5",
            name="f5",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="r5_f5",
                to="home.CustomText",
            ),
        ),
    ]
