# Generated by Django 2.2 on 2021-11-06 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0007_auto_20211106_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='upload.png', upload_to='media/images/'),
        ),
    ]