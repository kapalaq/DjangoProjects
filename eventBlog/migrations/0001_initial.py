# Generated by Django 4.2.11 on 2024-05-03 13:14

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('price', models.IntegerField(verbose_name='price (KZT)')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('created_on', models.DateTimeField(default=datetime.datetime(2024, 5, 3, 13, 14, 23, 736868, tzinfo=datetime.timezone.utc))),
                ('posted_on', models.DateTimeField(blank=True, null=True)),
                ('poster', models.ImageField(blank=True, null=True, upload_to='posters/%Y/%m/%d/')),
                ('place', models.CharField(blank=True, max_length=500, null=True)),
                ('phone', models.CharField(blank=True, max_length=24, null=True)),
                ('url', models.URLField(blank=True, max_length=300, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]