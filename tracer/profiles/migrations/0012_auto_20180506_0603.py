# Generated by Django 2.0.3 on 2018-05-05 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0011_auto_20180506_0547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='civil_status',
            field=models.IntegerField(blank=True, choices=[(0, 'Single'), (1, 'Married'), (2, 'Separated'), (3, 'Living Together'), (4, 'Divorced'), (5, 'Widow')], null=True),
        ),
    ]
