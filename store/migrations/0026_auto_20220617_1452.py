# Generated by Django 3.0.5 on 2022-06-17 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0025_auto_20220617_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='econtact',
            field=models.CharField(default=0, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supplier',
            name='eemail',
            field=models.CharField(default=0, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supplier',
            name='emob_no',
            field=models.CharField(default=0, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supplier',
            name='ename',
            field=models.CharField(default=0, max_length=120),
            preserve_default=False,
        ),
    ]
