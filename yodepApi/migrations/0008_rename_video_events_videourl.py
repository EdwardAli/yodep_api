# Generated by Django 4.1.3 on 2022-11-24 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yodepApi', '0007_events'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='video',
            new_name='videoUrl',
        ),
    ]