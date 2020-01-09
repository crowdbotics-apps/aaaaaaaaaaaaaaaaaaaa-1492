# Generated by Django 2.2.9 on 2020-01-09 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0009_r5_f5"),
    ]

    operations = [
        migrations.CreateModel(
            name="R56",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "f1",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="r56_f1",
                        to="home.R1",
                    ),
                ),
            ],
        ),
    ]
