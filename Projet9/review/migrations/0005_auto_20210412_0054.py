# Generated by Django 3.1.4 on 2021-04-11 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0004_auto_20210411_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
