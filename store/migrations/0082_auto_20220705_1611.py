# Generated by Django 3.1.12 on 2022-07-05 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0081_cost_grade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cost_grade',
            name='grade',
        ),
        migrations.DeleteModel(
            name='demo',
        ),
        migrations.DeleteModel(
            name='cost_grade',
        ),
    ]
