# Generated by Django 4.1.5 on 2023-02-04 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='csvfile',
            name='timeframe',
            field=models.IntegerField(default=10),
        ),
    ]
