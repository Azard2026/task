# Generated by Django 4.2.7 on 2023-11-28 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companywebsite', '0004_alter_contact_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='datetime',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]