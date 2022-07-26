# Generated by Django 3.2.13 on 2022-07-26 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='csvs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LatD', models.CharField(blank=True, max_length=50, null=True)),
                ('LatM', models.CharField(blank=True, max_length=50, null=True)),
                ('LatS', models.CharField(blank=True, max_length=50, null=True)),
                ('NS', models.CharField(blank=True, max_length=50, null=True)),
                ('LonD', models.CharField(blank=True, max_length=50, null=True)),
                ('LonM', models.CharField(blank=True, max_length=50, null=True)),
                ('LonS', models.CharField(blank=True, max_length=50, null=True)),
                ('EW', models.CharField(blank=True, max_length=50, null=True)),
                ('City', models.CharField(blank=True, max_length=50, null=True)),
                ('State', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custlis', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('utility_name', models.CharField(blank=True, max_length=200, null=True)),
                ('utility_short_name', models.CharField(blank=True, max_length=50, null=True)),
                ('utility_state', models.CharField(blank=True, max_length=50, null=True)),
                ('utility_district', models.CharField(blank=True, max_length=50, null=True)),
                ('utility_country', models.CharField(blank=True, max_length=50, null=True)),
                ('utility_postalcode', models.CharField(blank=True, max_length=20, null=True)),
                ('utility_address', models.TextField(blank=True, max_length=200, null=True)),
                ('contact_person', models.CharField(blank=True, max_length=200, null=True)),
                ('contact_email', models.EmailField(blank=True, max_length=50, null=True)),
                ('contact_phnum', models.CharField(blank=True, max_length=15, null=True)),
                ('contact_mobile', models.CharField(blank=True, max_length=15, null=True)),
                ('contact_designation', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_landline', models.CharField(blank=True, max_length=20, null=True)),
                ('emergency_person', models.CharField(blank=True, max_length=200, null=True)),
                ('emergency_altperson', models.CharField(blank=True, max_length=200, null=True)),
                ('emergency_mobile', models.CharField(blank=True, max_length=200, null=True)),
                ('emergency_altmobile', models.CharField(blank=True, max_length=200, null=True)),
                ('emergency_officeaddress', models.TextField(blank=True, max_length=200, null=True)),
                ('emergency_altofficeaddress', models.TextField(blank=True, max_length=200, null=True)),
                ('info_created_at', models.DateTimeField(auto_now_add=True)),
                ('info_updated_at', models.DateTimeField(auto_now=True)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.applists')),
            ],
        ),
    ]
