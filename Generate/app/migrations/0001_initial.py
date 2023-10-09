# Generated by Django 3.2.20 on 2023-09-22 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CertificateRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server_ip', models.GenericIPAddressField()),
                ('device_type', models.CharField(max_length=100)),
                ('site_id', models.IntegerField()),
                ('customer_name', models.CharField(max_length=255)),
                ('model_name', models.CharField(max_length=100)),
                ('project_type', models.CharField(max_length=100)),
            ],
        ),
    ]
