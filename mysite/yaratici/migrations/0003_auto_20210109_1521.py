# Generated by Django 3.1.4 on 2021-01-09 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yaratici', '0002_auto_20210109_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='edit_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
