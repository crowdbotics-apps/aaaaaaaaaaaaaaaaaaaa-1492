# Generated by Django 2.2.9 on 2020-01-09 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0006_r6"),
    ]

    operations = [
        migrations.AddField(
            model_name="r1",
            name="f4",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="r1_f4",
                to="home.HomePage",
            ),
        ),
    ]