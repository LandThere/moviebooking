# Generated by Django 4.0 on 2022-11-23 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browsing', '0003_alter_movie_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]
