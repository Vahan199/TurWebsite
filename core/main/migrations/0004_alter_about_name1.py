# Generated by Django 4.0.6 on 2022-07-17 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='name1',
            field=models.CharField(max_length=70, verbose_name='About name1'),
        ),
    ]
