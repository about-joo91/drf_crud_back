# Generated by Django 4.0.5 on 2022-06-26 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_postmodel_created_at_postmodel_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
