# Generated by Django 2.2.6 on 2020-08-18 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Place', '0012_auto_20200819_0322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placeline',
            name='checkedUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Place.CheckedUser'),
        ),
    ]
