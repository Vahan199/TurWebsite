# Generated by Django 4.0.6 on 2022-07-18 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_karciqner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='karciqner',
            name='name',
        ),
        migrations.AddField(
            model_name='karciqner',
            name='name1',
            field=models.CharField(default=1, max_length=50, verbose_name='Karc name1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='karciqner',
            name='name2',
            field=models.CharField(max_length=40, null=True, verbose_name='Karc name2'),
        ),
        migrations.AlterField(
            model_name='karciqner',
            name='about',
            field=models.TextField(verbose_name='Karc about'),
        ),
        migrations.AlterField(
            model_name='karciqner',
            name='img',
            field=models.ImageField(upload_to='media', verbose_name='Karc image'),
        ),
    ]
