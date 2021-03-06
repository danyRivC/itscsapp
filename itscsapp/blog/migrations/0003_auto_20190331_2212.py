# Generated by Django 2.0.13 on 2019-03-31 22:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_postblog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='postblog',
            name='created',
            field=models.DateField(auto_now=True, verbose_name='Fecha de creacion'),
        ),
        migrations.AddField(
            model_name='postblog',
            name='updated',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Ultima fecha de actualizacion'),
            preserve_default=False,
        ),
    ]
