# Generated by Django 3.2.13 on 2022-07-15 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0106_auto_20220713_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='metaln',
            field=models.CharField(choices=[('Zn', 'Zn'), ('ALU', 'ALU')], default=('Zn', 'Zn'), max_length=120),
        ),
        migrations.AlterField(
            model_name='grade',
            name='metaln2',
            field=models.CharField(choices=[('Zn', 'Zn'), ('ALU', 'ALU')], default=('Zn', 'Zn'), max_length=120),
        ),
    ]