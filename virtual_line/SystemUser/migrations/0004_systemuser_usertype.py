# Generated by Django 2.2.6 on 2020-08-15 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SystemUser', '0003_auto_20200816_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemuser',
            name='userType',
            field=models.ManyToManyField(to='SystemUser.UserType'),
        ),
    ]
