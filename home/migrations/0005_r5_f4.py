# Generated by Django 2.2.9 on 2020-01-09 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_r5'),
    ]

    operations = [
        migrations.AddField(
            model_name='r5',
            name='f4',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
