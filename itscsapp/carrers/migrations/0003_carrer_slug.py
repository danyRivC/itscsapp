# Generated by Django 2.0.13 on 2019-03-27 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrers', '0002_auto_20190319_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrer',
            name='slug',
            field=models.SlugField(default=2),
            preserve_default=False,
        ),
    ]