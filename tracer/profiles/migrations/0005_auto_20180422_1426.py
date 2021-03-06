# Generated by Django 2.0.3 on 2018-04-22 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20180422_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='competency_analytical',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='competency_comm',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='competency_computer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='competency_entrepreneurial',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='competency_leadership',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='competency_learning_efficiency',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='competency_mathematical',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='competency_other_reasons',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='competency_others',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='competency_problem_solving',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='competency_research',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='socail_trans_other_reason',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='social_trans_community_rel',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='social_trans_dialogue',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='social_trans_environment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='social_trans_family_rel',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='social_trans_leadership',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='social_trans_other',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='social_trans_peace',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='social_trans_spiritual',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='value_status_excellence',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='value_status_faith',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='value_status_integrity',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='value_status_respect',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='value_status_service',
            field=models.BooleanField(default=False),
        ),
    ]
