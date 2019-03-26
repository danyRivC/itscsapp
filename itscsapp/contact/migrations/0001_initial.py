# Generated by Django 2.0.13 on 2019-03-19 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('phone_number', models.CharField(max_length=255, verbose_name='Numero De Telefono')),
                ('subject', models.CharField(max_length=255, verbose_name='Asunto')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('message', models.TextField(verbose_name='Mensaje')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')),
            ],
            options={
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'contactos',
                'ordering': ['-created'],
            },
        ),
    ]