# Generated by Django 2.2.9 on 2020-01-09 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0013_r6_f6"),
        ("users", "0002_auto_20200109_1525"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="f1",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_f1",
                to="home.HomePage",
            ),
        ),
    ]
