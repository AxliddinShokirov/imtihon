# Generated by Django 5.0.7 on 2024-07-13 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_banner_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='description',
            field=models.CharField(max_length=3000),
        ),
    ]
