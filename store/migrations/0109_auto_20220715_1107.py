# Generated by Django 3.2.13 on 2022-07-15 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0108_auto_20220715_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='metaln',
            field=models.CharField(choices=[], max_length=120),
        ),
        migrations.AlterField(
            model_name='grade',
            name='metaln2',
            field=models.CharField(choices=[], max_length=120),
        ),
    ]