# Generated by Django 3.2.6 on 2022-06-25 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0054_alter_grade_metalc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='metalc',
            field=models.IntegerField(default=()),
        ),
    ]
