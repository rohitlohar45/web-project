# Generated by Django 3.0.5 on 2022-06-17 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0033_auto_20220617_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='typeo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Typeo'),
        ),
    ]
