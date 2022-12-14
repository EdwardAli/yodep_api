# Generated by Django 4.1.4 on 2022-12-12 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yodepApi', '0013_vacancy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, null=True, upload_to='files/testimonial')),
                ('body', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Testimony',
        ),
    ]
