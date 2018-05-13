from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, HTML, MultiField, Fieldset
from django.forms import ModelForm

from . import models

class ProfileForm(ModelForm):
    class Meta:
        model = models.Profile
        fields = [
            'photo',
            'student_number',
            'degree',
            'specialization',
            'year_graduated_ndu',
            'last_name',
            'first_name',
            'middle_name',
            'name_ext',
            'address',
            'birthdate',
            'gender',
            'civil_status',
            'preferred_mailing_address',
            'alternate_email',
            'contact_numbers',
            'is_natl_lic_exam_passer',
            'field_exam_passed',
            'field_exam_year_passed',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))


class SurveyForm(ModelForm):
    class Meta:
        model = models.Survey
        fields = [
            'user',
            'is_presently_employed',
            'year_started',
            'employment_status',
            'job_position',
            'employer',
            'employer_address',
            'unemployed_advance_study',
            'unemployed_family_concern',
            'unemployed_health',
            'unemployed_no_opp',
            'unemployed_did_not_look_for_job',
            'unemployed_lack_experience',
            'unemployed_others',
            'value_faith',
            'value_integrity',
            'value_respect',
            'value_excellence',
            'value_service',
            'social_environment_ed',
            'social_dialogue',
            'social_spiritual',
            'social_leadership',
            'social_family_rel',
            'social_community_rel',
            'social_peace_advocacy',
            'competency_comm',
            'competency_analytical',
            'competency_entrepreneurial',
            'competency_research',
            'competency_math',
            'competency_leadership',
            'competency_human_rel',
            'competency_cit',
            'competency_learning_efficiency',
            'other_ndu_alumni',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        labels = {
            'is_presently_employed': 'Yes',
            'employment_status': 'Please indicate the STATUS at your PRESENT EMPLOYMENT',
             'job_position': 'Your present job position',
             'employer': 'Name of employer/company',
             'employer_address': 'Address of Employer/Company',
             'unemployed_advance_study': 'Advance/Futher study',
             'unemployed_family_concern': 'Family concern',
             'unemployed_health': 'Health-related reason(s)',
             'unemployed_no_opp': 'No job opportunity',
             'unemployed_did_not_look_for_job': 'Did not look for a job',
             'unemployed_lack_experience': 'Lack of work experience',
             'unemployed_others': 'Other(s)',
             'value_faith': 'Faith',
             'value_integrity': 'Integrity',
             'value_respect': 'Respect',
             'value_excellence': 'Excellence',
             'value_service': 'Service',
             'social_environment_ed': 'Environment Education',
             'social_dialogue': 'Dialogue',
             'social_spiritual': 'Spiritual',
             'social_leadership': 'Leadership',
             'social_family_rel': 'Family relations',
             'social_community_rel': 'Community relations',
             'social_peace_advocacy': 'Peace advocacy',
             'competency_comm': 'Communication skills (verbal & written)',
             'competency_analytical': 'Analytical/Critical thinking skills',
             'competency_entrepreneurial': 'Entrepreneurial/Sales and marketing skills',
             'competency_research': 'Research skills',
             'competency_math': 'Mathematical and statistical skills',
             'competency_leadership': 'Leadership skills',
             'competency_human_rel': 'Human relation',
             'competency_cit': 'Computer information technology',
             'competency_learning_efficiency': 'Learning efficiency',
             'other_ndu_alumni': 'Being one of the alumni of NDU, kindly list down other NDU alumni whom you know that have graduated in School Years 2011-2012 to 2015-2016. Their participation will contribute to the success of this study. (Name, Full Address, Contact No. and E-mail Address)',

        }
        for k, v in labels.items():
            self.fields[k].label = v

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('user', type='hidden'),
            HTML('<h2>Employment Background</h2>'),
            HTML('<p><strong>Are you presently employed? Please check:</strong></p>'),
            'is_presently_employed',
            'year_started',
            'employment_status',
            'job_position',
            'employer',
            'employer_address',
            HTML('<p><strong>No/Never been Employed, Please state reason(s) why you are not yet employed. You may check more than one answer.</strong></p>'),
            'unemployed_advance_study',
            'unemployed_family_concern',
            'unemployed_health',
            'unemployed_no_opp',
            'unemployed_did_not_look_for_job',
            'unemployed_lack_experience',
            'unemployed_others',
            HTML('<h2>Values and Competencies</h2>'),
            HTML('<p><strong>What values from your Oblate Education (NDU) which you find mose useful/relevant to your career? You may check more than one answer.</strong></p>'),
            'value_faith',
            'value_integrity',
            'value_respect',
            'value_excellence',
            'value_service',
            HTML('<p><strong>How have these values been instrumental to Social Transformation in relation to your work or profession?</strong></p>'),
            'social_environment_ed',
            'social_dialogue',
            'social_spiritual',
            'social_leadership',
            'social_family_rel',
            'social_community_rel',
            'social_peace_advocacy',
            HTML('<p><strong>What competencies acquired in college do you find very useful in your job? You may check more than one answer.</strong></p>'),
            'competency_comm',
            'competency_analytical',
            'competency_entrepreneurial',
            'competency_research',
            'competency_math',
            'competency_leadership',
            'competency_human_rel',
            'competency_cit',
            'competency_learning_efficiency',
            'other_ndu_alumni',
            Submit('submit', 'Submit')

        )
