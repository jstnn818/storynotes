# Generated by Django 4.2.5 on 2024-02-08 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0004_story_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
