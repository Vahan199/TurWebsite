# Generated by Django 4.0.6 on 2022-07-17 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_amragir_apranqner_champordvayr'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogbg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='blogbg name')),
                ('name2', models.CharField(max_length=50, verbose_name='blogbg name2')),
                ('img', models.ImageField(upload_to='media', verbose_name='blogbg image')),
            ],
            options={
                'verbose_name': 'Blogbg',
                'verbose_name_plural': 'Blogbgs',
            },
        ),
        migrations.CreateModel(
            name='Hayvayr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='hayvayr name')),
                ('about', models.TextField(verbose_name='hayrvayr name')),
                ('img', models.ImageField(upload_to='media', verbose_name='hayvayr img')),
            ],
            options={
                'verbose_name': 'Hayvayr',
                'verbose_name_plural': 'Hayvayrs',
            },
        ),
    ]