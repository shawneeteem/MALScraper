# Generated by Django 2.1.7 on 2019-03-12 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0004_auto_20190312_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='episodes',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='show',
            name='rating',
            field=models.FloatField(),
        ),
    ]