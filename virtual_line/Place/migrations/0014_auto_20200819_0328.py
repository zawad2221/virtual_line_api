# Generated by Django 2.2.6 on 2020-08-18 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Place', '0013_auto_20200819_0326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placeline',
            name='checkedUser',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='Place.CheckedUser'),
            preserve_default=False,
        ),
    ]
