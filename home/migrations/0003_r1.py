# Generated by Django 2.2.9 on 2020-01-09 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_load_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='R1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.DateField()),
                ('f2', models.DateTimeField(auto_now=True)),
                ('f3', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]
