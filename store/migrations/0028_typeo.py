# Generated by Django 3.0.5 on 2022-06-17 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0027_auto_20220617_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='typeo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=10)),
            ],
        ),
    ]
