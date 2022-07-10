# Generated by Django 3.1.12 on 2022-07-06 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0091_auto_20220706_1145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demo',
            name='name',
        ),
        migrations.AddField(
            model_name='demo',
            name='duty',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='demo',
            name='grade',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='store.grade'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='demo',
            name='metalw',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='demo',
            name='metalw1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='demo',
            name='metalw10',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='demo',
            name='metalw11',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='demo',
            name='metalw12',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='demo',
            name='metalw13',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='demo',
            name='metalw14',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='demo',
            name='metalw15',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='demo',
            name='metalw16',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='demo',
            name='metalw17',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='demo',
            name='metalw18',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='demo',
            name='metalw19',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='demo',
            name='metalw2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='demo',
            name='metalw20',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='demo',
            name='metalw3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='demo',
            name='metalw4',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='demo',
            name='metalw5',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='demo',
            name='metalw6',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='demo',
            name='metalw7',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='demo',
            name='metalw8',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='demo',
            name='metalw9',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='demo',
            name='metalwc',
            field=models.IntegerField(default=0),
        ),
    ]
