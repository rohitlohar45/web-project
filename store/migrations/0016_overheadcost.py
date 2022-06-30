# Generated by Django 3.0.5 on 2022-06-07 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_auto_20220607_1332'),
    ]

    operations = [
        migrations.CreateModel(
            name='OverheadCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('cost', models.IntegerField(max_length=220)),
                ('yard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Yard')),
            ],
        ),
    ]
