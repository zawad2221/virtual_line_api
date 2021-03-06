# Generated by Django 2.2.6 on 2020-08-16 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Place', '0003_auto_20200817_0453'),
    ]

    operations = [
        migrations.AddField(
            model_name='placeinformation',
            name='placeLine',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Place.PlaceLine'),
        ),
        migrations.AddField(
            model_name='placeinformation',
            name='placeType',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Place.PlaceType'),
        ),
    ]
