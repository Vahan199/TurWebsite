# Generated by Django 4.0.6 on 2022-07-15 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeBG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=30, verbose_name='BG name1')),
                ('name2', models.CharField(max_length=30, verbose_name='BG name2')),
                ('about', models.TextField(verbose_name='BG about')),
                ('img', models.ImageField(upload_to='media', verbose_name='BG image')),
            ],
            options={
                'verbose_name': 'HomeBG',
                'verbose_name_plural': 'HomeBGS',
            },
        ),
    ]
