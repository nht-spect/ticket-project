# Generated by Django 2.2 on 2021-12-05 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0032_auto_20211205_1421'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
            ],
        ),
    ]