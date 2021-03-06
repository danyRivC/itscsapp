# Generated by Django 2.0.13 on 2019-03-20 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carrers', '0002_auto_20190319_2041'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificaicon')),
                ('content', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('carrer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='carrers.Carrer')),
            ],
            options={
                'ordering': ['-created', 'updated'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]
