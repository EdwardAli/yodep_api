# Generated by Django 4.1.3 on 2022-11-24 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yodepApi', '0004_career_alter_project_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('location', models.CharField(max_length=250)),
                ('image', models.ImageField(blank=True, null=True, upload_to='files/gallary')),
            ],
        ),
    ]