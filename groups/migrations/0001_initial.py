# Generated by Django 3.2.6 on 2022-07-27 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_profile_apps'),
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=800)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.applists')),
                ('members', models.ManyToManyField(to='accounts.Profile')),
            ],
        ),
    ]
