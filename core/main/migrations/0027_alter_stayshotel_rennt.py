# Generated by Django 4.0.6 on 2022-07-28 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_stayshotel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stayshotel',
            name='rennt',
            field=models.CharField(choices=[('R', 'for Rent'), ('S', 'for Shell')], default='R', max_length=10),
        ),
    ]
