# Generated by Django 3.2.20 on 2023-09-22 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20230922_0530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificaterequest',
            name='customer_name',
            field=models.CharField(max_length=255),
        ),
    ]
