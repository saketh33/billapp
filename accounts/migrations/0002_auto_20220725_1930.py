# Generated by Django 3.2.13 on 2022-07-25 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='cust',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
    ]