# Generated by Django 4.1.3 on 2022-11-25 09:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yodepApi', '0008_rename_video_events_videourl'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogTitle', models.CharField(max_length=250)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('image', models.ImageField(upload_to='files/blog')),
                ('subTitle', models.CharField(blank=True, max_length=250, null=True)),
                ('body', models.TextField()),
            ],
        ),
    ]
