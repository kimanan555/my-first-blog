# Generated by Django 2.0.9 on 2018-12-14 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20181214_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dt2',
            name='Ec',
            field=models.FloatField(max_length=3),
        ),
        migrations.AlterField(
            model_name='dt2',
            name='Water',
            field=models.FloatField(max_length=3),
        ),
        migrations.AlterField(
            model_name='dt2',
            name='pH',
            field=models.FloatField(max_length=3),
        ),
        migrations.AlterField(
            model_name='dt2',
            name='temp',
            field=models.FloatField(max_length=3),
        ),
    ]
