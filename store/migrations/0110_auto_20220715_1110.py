# Generated by Django 3.2.13 on 2022-07-15 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0109_auto_20220715_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='metaln',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='grade',
            name='metaln2',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
