# Generated by Django 2.0.2 on 2018-10-07 18:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MovieReview', '0001_initial'),
    ]

    operations = [
            migrations.AddField(
            model_name='movieinfo',
            name='movie_type',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
