# Generated by Django 2.0.2 on 2018-10-08 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieReview', '0008_movieinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='movieinfo',
            name='movie_details',
            field=models.TextField(default=' ', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movieinfo',
            name='movie_release_date',
            field=models.CharField(default=' ', max_length=35),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movieinfo',
            name='movie_type',
            field=models.CharField(default=' ', max_length=200),
            preserve_default=False,
        ),
    ]