# Generated by Django 4.0.5 on 2022-06-25 13:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postmodel',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]
