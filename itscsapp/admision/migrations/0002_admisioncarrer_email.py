# Generated by Django 2.0.13 on 2019-03-31 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admision', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='admisioncarrer',
            name='email',
            field=models.EmailField(default=1, max_length=254, verbose_name='Email'),
            preserve_default=False,
        ),
    ]
