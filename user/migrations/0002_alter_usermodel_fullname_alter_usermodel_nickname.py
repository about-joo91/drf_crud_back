# Generated by Django 4.0.5 on 2022-06-25 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='fullname',
            field=models.CharField(max_length=100, verbose_name='fullname'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='nickname',
            field=models.CharField(max_length=100, verbose_name='nickname'),
        ),
    ]
