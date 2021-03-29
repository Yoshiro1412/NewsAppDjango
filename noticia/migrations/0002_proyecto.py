# Generated by Django 3.1.5 on 2021-01-12 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('state', models.CharField(choices=[('P', 'In Progress'), ('F', 'Finished')], max_length=1)),
                ('main_topic', models.CharField(choices=[('Waste', 'Waste'), ('Economy', 'Economy')], max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
