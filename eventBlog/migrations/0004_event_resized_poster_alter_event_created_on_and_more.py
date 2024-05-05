# Generated by Django 4.2.11 on 2024-05-05 17:17

import datetime
from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('eventBlog', '0003_alter_event_options_alter_event_created_on_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='resized_poster',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[640, 360], upload_to='resized_image'),
        ),
        migrations.AlterField(
            model_name='event',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 5, 17, 17, 22, 194209, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
    ]
