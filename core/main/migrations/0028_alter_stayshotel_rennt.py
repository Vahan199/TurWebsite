# Generated by Django 4.0.6 on 2022-07-28 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_alter_stayshotel_rennt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stayshotel',
            name='rennt',
            field=models.CharField(choices=[('for Rent', ' Rent'), ('for Shell', ' Shell')], default='for Rent', max_length=10),
        ),
    ]