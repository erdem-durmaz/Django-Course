# Generated by Django 3.1.4 on 2021-01-09 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yaratici', '0009_auto_20210109_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='meta_description',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='meta_tags',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
