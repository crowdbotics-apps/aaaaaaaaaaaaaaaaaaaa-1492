# Generated by Django 2.2.9 on 2020-02-11 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0014_xxx1"),
    ]

    operations = [
        migrations.AddField(
            model_name="xxx1",
            name="r111",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="xxx1_r111",
                to="home.CustomText",
            ),
        ),
    ]
