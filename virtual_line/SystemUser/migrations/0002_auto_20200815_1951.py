# Generated by Django 2.2.6 on 2020-08-15 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SystemUser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systemuser',
            name='phoneNumber',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
