# Generated by Django 2.2 on 2021-11-06 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0003_remove_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='defaut.png', upload_to=''),
        ),
    ]