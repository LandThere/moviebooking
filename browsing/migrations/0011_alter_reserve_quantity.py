# Generated by Django 4.0 on 2022-11-30 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browsing', '0010_alter_movie_quantity_alter_reserve_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserve',
            name='quantity',
            field=models.IntegerField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default=0, null=True),
        ),
    ]
