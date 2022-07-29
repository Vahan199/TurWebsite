# Generated by Django 4.0.6 on 2022-07-17 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_mezhet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amragir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='amrqagir name')),
                ('about', models.TextField(verbose_name='amragir about')),
                ('img', models.ImageField(upload_to='media', verbose_name='amragir image')),
            ],
            options={
                'verbose_name': 'Amragir',
                'verbose_name_plural': 'Amragirs',
            },
        ),
        migrations.CreateModel(
            name='Apranqner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='apranq name')),
                ('price', models.IntegerField(verbose_name='apranq price')),
                ('img', models.ImageField(upload_to='media', verbose_name='apranq image')),
            ],
            options={
                'verbose_name': 'Apranqer',
                'verbose_name_plural': 'Apranqners',
            },
        ),
        migrations.CreateModel(
            name='ChampordVayr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='vayr name')),
                ('about', models.TextField(verbose_name='vayr about')),
                ('img', models.ImageField(upload_to='media', verbose_name='vayr image')),
            ],
            options={
                'verbose_name': 'ChampordVayr',
                'verbose_name_plural': 'ChampordVayrs',
            },
        ),
    ]