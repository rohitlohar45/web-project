# Generated by Django 3.2.13 on 2022-07-17 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0110_auto_20220715_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quality',
            name='metalw',
            field=models.FloatField(default=0),
        ),
    ]
