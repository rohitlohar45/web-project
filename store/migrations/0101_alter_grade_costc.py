# Generated by Django 3.2.13 on 2022-07-10 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0100_alter_grade_costc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='costc',
            field=models.FloatField(default=0, null=True),
        ),
    ]
