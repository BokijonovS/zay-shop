# Generated by Django 5.0.6 on 2024-05-21 13:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_brand_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='users/')),
                ('phone', models.CharField(blank=True, max_length=13, null=True, verbose_name='Phone number')),
                ('mobile', models.CharField(blank=True, max_length=13, null=True, verbose_name='Mobile')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('site', models.URLField(blank=True, max_length=50, null=True)),
                ('job', models.CharField(blank=True, max_length=50, null=True)),
                ('job2', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Custom user',
                'verbose_name_plural': 'Custom users',
                'ordering': ['-pk'],
            },
        ),
    ]
