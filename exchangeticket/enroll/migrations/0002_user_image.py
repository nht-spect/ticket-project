# Generated by Django 2.2 on 2021-11-06 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.FileField(default='', upload_to=''),
        ),
    ]