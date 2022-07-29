# Generated by Django 4.0.6 on 2022-07-26 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_flightspay_flights_name4_flights_name5_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='flightspay',
            name='name2',
            field=models.CharField(max_length=20, null=True, verbose_name='flightpays name2'),
        ),
        migrations.AddField(
            model_name='flightspay',
            name='name3',
            field=models.CharField(max_length=20, null=True, verbose_name='flightpays name3'),
        ),
        migrations.AddField(
            model_name='flightspay',
            name='name4',
            field=models.CharField(max_length=20, null=True, verbose_name='flightpays name4'),
        ),
        migrations.AlterField(
            model_name='flights',
            name='name4',
            field=models.CharField(max_length=20, null=True, verbose_name='flights name4'),
        ),
        migrations.AlterField(
            model_name='flights',
            name='name5',
            field=models.CharField(max_length=20, null=True, verbose_name='flights name5'),
        ),
        migrations.AlterField(
            model_name='flightspay',
            name='name',
            field=models.CharField(max_length=20, verbose_name='flightpays name'),
        ),
    ]
