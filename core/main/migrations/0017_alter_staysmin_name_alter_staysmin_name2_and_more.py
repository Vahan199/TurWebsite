# Generated by Django 4.0.6 on 2022-07-21 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_staysmin_name_alter_staysmin_name2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staysmin',
            name='name',
            field=models.IntegerField(blank=True, null=True, verbose_name='staysmin name'),
        ),
        migrations.AlterField(
            model_name='staysmin',
            name='name2',
            field=models.IntegerField(blank=True, null=True, verbose_name='staysmin name1'),
        ),
        migrations.AlterField(
            model_name='staysmin',
            name='name3',
            field=models.IntegerField(blank=True, null=True, verbose_name='staysmin name2'),
        ),
        migrations.AlterField(
            model_name='staysmin',
            name='name4',
            field=models.IntegerField(blank=True, null=True, verbose_name='staysmin name3'),
        ),
        migrations.AlterField(
            model_name='staysmin',
            name='name5',
            field=models.IntegerField(blank=True, null=True, verbose_name='staysmin name4'),
        ),
    ]
