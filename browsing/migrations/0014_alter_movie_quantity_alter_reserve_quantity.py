# Generated by Django 4.0 on 2022-11-30 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browsing', '0013_alter_reserve_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='quantity',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='reserve',
            name='quantity',
            field=models.FloatField(null=True),
        ),
    ]
