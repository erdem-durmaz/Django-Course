# Generated by Django 3.1.4 on 2021-01-03 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emailer', '0005_auto_20210103_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='comment',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]