# Generated by Django 3.2.13 on 2022-08-08 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p1app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='just', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
