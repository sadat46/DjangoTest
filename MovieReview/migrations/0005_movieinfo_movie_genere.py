# Generated by Django 2.0.2 on 2018-10-08 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieReview', '0004_movieinfo_movie_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='movieinfo',
            name='movie_genere',
            field=models.CharField(default=' ', max_length=20),
            preserve_default=False,
        ),
    ]