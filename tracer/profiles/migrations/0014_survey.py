# Generated by Django 2.0.3 on 2018-05-05 23:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0013_profile_field_exam_year_passed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_presently_employed', models.BooleanField(default=False)),
                ('year_started', models.IntegerField(blank=True, null=True)),
                ('employment_status', models.IntegerField(blank=True, choices=[(0, 'Regular/Permanent'), (1, 'Contractual/Temporary/Casual'), (2, 'Self-employed'), (3, 'Unpaid family worker'), (4, 'Wage/Salary worker')], null=True)),
                ('job_position', models.CharField(blank=True, default='', max_length=100)),
                ('employer', models.CharField(blank=True, default='', max_length=100)),
                ('employer_address', models.CharField(blank=True, default='', max_length=200)),
                ('unemployed_advance_study', models.BooleanField(default=False)),
                ('unemployed_family_concern', models.BooleanField(default=False)),
                ('unemployed_health', models.BooleanField(default=False)),
                ('unemployed_no_opp', models.BooleanField(default=False)),
                ('unemployed_did_not_look_for_job', models.BooleanField(default=False)),
                ('unemployed_lack_experience', models.BooleanField(default=False)),
                ('unemployed_others', models.BooleanField(default=False)),
                ('value_faith', models.BooleanField(default=False)),
                ('value_integrity', models.BooleanField(default=False)),
                ('value_respect', models.BooleanField(default=False)),
                ('value_excellence', models.BooleanField(default=False)),
                ('value_service', models.BooleanField(default=False)),
                ('social_environment_ed', models.BooleanField(default=False)),
                ('social_dialogue', models.BooleanField(default=False)),
                ('social_spiritual', models.BooleanField(default=False)),
                ('social_leadership', models.BooleanField(default=False)),
                ('social_family_rel', models.BooleanField(default=False)),
                ('social_community_rel', models.BooleanField(default=False)),
                ('social_peace_advocacy', models.BooleanField(default=False)),
                ('competency_comm', models.BooleanField(default=False)),
                ('competency_analytical', models.BooleanField(default=False)),
                ('competency_entrepreneurial', models.BooleanField(default=False)),
                ('competency_research', models.BooleanField(default=False)),
                ('competency_math', models.BooleanField(default=False)),
                ('competency_leadership', models.BooleanField(default=False)),
                ('competency_human_rel', models.BooleanField(default=False)),
                ('competency_cit', models.BooleanField(default=False)),
                ('competency_learning_efficiency', models.BooleanField(default=False)),
                ('other_ndu_alumni', models.TextField(blank=True, default='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
