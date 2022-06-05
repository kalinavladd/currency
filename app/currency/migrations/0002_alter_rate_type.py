# Generated by Django 4.0.2 on 2022-05-22 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Dollar'), (2, 'Euro')], default=1, null=True),
        ),
    ]
