# Generated by Django 3.2.13 on 2022-06-30 06:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=40, null=True)),
                ('city', models.CharField(blank=True, max_length=40, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('ph_num', models.CharField(blank=True, max_length=15, null=True)),
                ('xp', models.IntegerField(blank=True, default=100, null=True)),
                ('techsnap_cash', models.IntegerField(blank=True, default=999, null=True)),
                ('slug', models.SlugField(blank=True, editable=False, max_length=200, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='notifications')),
                ('mark_as_read', models.BooleanField(default=False)),
                ('body', models.TextField()),
                ('url', models.URLField(blank=True, null=True)),
                ('url_name', models.CharField(blank=True, default='View', max_length=255, null=True)),
                ('notified_time', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(editable=False, max_length=16, null=True, unique=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_notifications', to='accounts.profile')),
            ],
        ),
    ]
