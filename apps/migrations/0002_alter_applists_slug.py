# Generated by Django 3.2.6 on 2022-07-29 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applists',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True),
        ),
    ]
