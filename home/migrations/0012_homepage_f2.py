# Generated by Django 2.2.9 on 2020-01-09 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_r57'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='f2',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
