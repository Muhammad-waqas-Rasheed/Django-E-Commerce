# Generated by Django 3.1.1 on 2020-12-11 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0004_laptop_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(default='local', max_length=50),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='BlueTooth',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='GPS',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='Radio',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='WLAN',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='audio',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='browser',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='capacity',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='chipset',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='cpu',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='fastCharging',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='games',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='gpu',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='messaging',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='name',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='resolution',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='sensors',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='size',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='technology',
            field=models.CharField(default='null', max_length=50),
        ),
    ]
