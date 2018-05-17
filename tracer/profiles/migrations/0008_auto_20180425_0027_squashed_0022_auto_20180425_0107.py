# Generated by Django 2.0.3 on 2018-04-24 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('profiles', '0008_auto_20180425_0027'), ('profiles', '0009_auto_20180425_0033'), ('profiles', '0010_auto_20180425_0035'), ('profiles', '0011_auto_20180425_0037'), ('profiles', '0012_remove_profile_civil_status'), ('profiles', '0013_profile_civil_status'), ('profiles', '0014_remove_profile_gender'), ('profiles', '0015_profile_gender'), ('profiles', '0016_profile_specialization'), ('profiles', '0017_auto_20180425_0048'), ('profiles', '0018_profile_alternate_email'), ('profiles', '0019_auto_20180425_0056'), ('profiles', '0020_profile_preferred_mailing_address'), ('profiles', '0021_auto_20180425_0102'), ('profiles', '0022_auto_20180425_0107')]

    dependencies = [
        ('profiles', '0007_auto_20180422_1435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='student_num',
        ),
        migrations.AddField(
            model_name='profile',
            name='student_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='middle_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='name_ext',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.RemoveField(
            model_name='profile',
            name='gender',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='status',
            new_name='civil_status',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='civil_status',
        ),
        migrations.AddField(
            model_name='profile',
            name='civil_status',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.IntegerField(blank=True, choices=[(0, 'Male'), (1, 'Female')], null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='specialization',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.RemoveField(
            model_name='profile',
            name='year_graduated',
        ),
        migrations.AddField(
            model_name='profile',
            name='year_graduated_ndu',
            field=models.IntegerField(blank=True, null=True, verbose_name='year graduated from NDU'),
        ),
        migrations.AddField(
            model_name='profile',
            name='alternate_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='field_exam_passed',
            field=models.IntegerField(blank=True, choices=[(0, 'Accountancy (CPA)'), (1, 'Civil Engineering (CE)'), (2, 'Electrical Engineering (EE)'), (3, 'Mechanical Engineering (ME)'), (4, 'Librarians'), (5, 'Nursing'), (6, 'Professional Teachers (LET)'), (7, 'Guidance Counseling (GC)'), (8, 'Bar Examination (LAW)')], null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_natl_lic_exam_passer',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='profile',
            name='preferred_mailing_address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.RemoveField(
            model_name='profile',
            name='competency_analytical',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='competency_comm',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='competency_computer',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='competency_entrepreneurial',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='competency_leadership',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='competency_learning_efficiency',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='competency_mathematical',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='competency_other_reasons',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='competency_others',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='competency_problem_solving',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='competency_research',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='employement_status',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='employer_address',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='employer_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='employment_status_other',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='is_currently_employed',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='nature_of_work',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='present_job_position',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='socail_trans_other_reason',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='social_trans_community_rel',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='social_trans_dialogue',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='social_trans_environment',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='social_trans_family_rel',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='social_trans_leadership',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='social_trans_other',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='social_trans_peace',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='social_trans_spiritual',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='unemployed_advance_study',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='unemployed_did_not_look',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='unemployed_family_concern',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='unemployed_health',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='unemployed_lack_exp',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='unemployed_no_job_opportunity',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='unemployed_other',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='unemployed_other_reasons',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='value_status_excellence',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='value_status_faith',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='value_status_integrity',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='value_status_respect',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='value_status_service',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='year_started',
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='contact_numbers',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='degree',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='degree/course'),
        ),
    ]
