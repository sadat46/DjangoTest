# Generated by Django 2.0.2 on 2018-10-13 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20181013_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='upload',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
