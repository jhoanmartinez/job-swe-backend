# Generated by Django 4.2.5 on 2023-09-28 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='point_lat',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='point_long',
            field=models.FloatField(null=True),
        ),
    ]
