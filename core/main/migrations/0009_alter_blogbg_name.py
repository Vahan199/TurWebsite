# Generated by Django 4.0.6 on 2022-07-17 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_blogbg_hayvayr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogbg',
            name='name',
            field=models.TextField(verbose_name='blogbg name'),
        ),
    ]
