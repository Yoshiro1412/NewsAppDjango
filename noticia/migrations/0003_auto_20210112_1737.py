# Generated by Django 3.1.5 on 2021-01-12 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0002_proyecto'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='image',
            field=models.ImageField(null=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='image',
            field=models.ImageField(null=True, upload_to='uploads/'),
        ),
    ]
