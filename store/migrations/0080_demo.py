# Generated by Django 3.1.12 on 2022-07-05 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0079_delete_cost_grade'),
    ]

    operations = [
        migrations.CreateModel(
            name='demo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('details', models.CharField(max_length=120)),
                ('gradegrp', models.CharField(max_length=120)),
                ('misc', models.CharField(max_length=120)),
                ('metal', models.CharField(max_length=120)),
                ('metalc', models.CharField(max_length=120)),
                ('cost', models.CharField(max_length=120)),
                ('costc', models.CharField(max_length=120)),
            ],
        ),
    ]
