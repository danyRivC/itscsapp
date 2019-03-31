# Generated by Django 2.0.13 on 2019-03-31 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='Titulo')),
                ('content', models.TextField(verbose_name='Contenido')),
            ],
            options={
                'verbose_name': 'Entrada de Blog',
                'verbose_name_plural': 'Entradas del Blog',
            },
        ),
    ]
