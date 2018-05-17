from django.db import models
from django.conf import settings
from django.urls import reverse



class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    student_number = models.CharField(max_length=50, blank=True, default='')
    degree = models.CharField(
        'Degree/Course', max_length=100, blank=True, default='')
    specialization = models.CharField(max_length=100, blank=True, default='') 
    year_graduated_ndu = models.IntegerField(
        'year graduated from NDU', blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, default='')
    first_name = models.CharField(max_length=50, blank=True, default='')
    middle_name = models.CharField(max_length=50, blank=True, default='')
    name_ext = models.CharField(max_length=50, blank=True, default='')
    address = models.CharField(max_length=200, blank=True, default='')
    birthdate = models.DateField(blank=True, null=True)

    GENDER_CHOICES = (
        (0, 'Male'),
        (1, 'Female')
    )
    gender = models.IntegerField(choices=GENDER_CHOICES, blank=True, null=True)

    CIVIL_STATUS_CHOICES = (
        (0, 'Single'),
        (1, 'Married'),
        (2, 'Separated'),
        (3, 'Living Together'),
        (4, 'Divorced'),
        (5, 'Widow/Widower')
    )
    civil_status = models.IntegerField(
        choices=CIVIL_STATUS_CHOICES, blank=True, null=True)

    preferred_mailing_address = models.CharField(
        max_length=200, blank=True, default='')

    alternate_email = models.EmailField(blank=True, null=True)
    contact_numbers = models.CharField(max_length=100, blank=True, default='')

    is_natl_lic_exam_passer = models.NullBooleanField(blank=True, null=True)

    FIELD_EXAM_PASSED_CHOICES = (
        (0, 'Accountancy (CPA)'),
        (1, 'Civil Engineering (CE)'),
        (2, 'Electrical Engineering (EE)'),
        (3, 'Mechanical Engineering (ME)'),
        (4, 'Librarians'),
        (5, 'Nursing'),
        (6, 'Professional Teachers (LET)'),
        (7, 'Guidance Counseling (GC)'),
        (8, 'Bar Examination (LAW)')
    )
    field_exam_passed = models.IntegerField(
        choices=FIELD_EXAM_PASSED_CHOICES, blank=True, null=True)

    field_exam_year_passed = models.IntegerField(
        blank=True, null=True
    )

    def __str__(self):
        return (
            f'{self.user.username} '
            f'({self.full_name})'
        )

    def get_absolute_url(self):
        return reverse('profile-detail', kwargs={'pk': self.pk})

    @property
    def full_name(self):
        return (
            f'{self.last_name}, {self.first_name} {self.name_ext} '
            f'{self.middle_name}'
        )

    def get_update_url(self):
        return reverse('profile-update', kwargs={'pk': self.pk})


class Survey(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    is_presently_employed = models.BooleanField(blank=True, default=False)
    year_started = models.IntegerField(blank=True, null=True)

    EMPLOYMENT_STATUS_CHOICES = (
        (0, 'Regular/Permanent'),
        (1, 'Contractual/Temporary/Casual'),
        (2, 'Self-employed'),
        (3, 'Unpaid family worker'),
        (4, 'Wage/Salary worker')
    )
    employment_status = models.IntegerField(
        choices=EMPLOYMENT_STATUS_CHOICES, blank=True, null=True
    )
    job_position = models.CharField(max_length=100, blank=True, default='')
    employer = models.CharField(max_length=100, blank=True, default='')
    employer_address = models.CharField(max_length=200, blank=True, default='')

    unemployed_advance_study = models.BooleanField(
        blank=True, default=False)
    unemployed_family_concern = models.BooleanField(
        blank=True, default=False
    )
    unemployed_health = models.BooleanField(
        blank=True, default=False
    )
    unemployed_no_opp = models.BooleanField(
        blank=True, default=False
    )
    unemployed_did_not_look_for_job = models.BooleanField(
        blank=True, default=False
    )
    unemployed_lack_experience = models.BooleanField(
        blank=True, default=False
    )
    unemployed_others = models.BooleanField(
        blank=True, default=False
    )

    value_faith = models.BooleanField(
        blank=True, default=False
    )
    value_integrity = models.BooleanField(
        blank=True, default=False
    )
    value_respect = models.BooleanField(
        blank=True, default=False
    )
    value_excellence = models.BooleanField(
        blank=True, default=False
    )
    value_service = models.BooleanField(
        blank=True, default=False
    )

    social_environment_ed = models.BooleanField(
        blank=True, default=False
    )
    social_dialogue = models.BooleanField(
        blank=True, default=False
    )
    social_spiritual = models.BooleanField(
        blank=True, default=False
    )
    social_leadership = models.BooleanField(
        blank=True, default=False
    )
    social_family_rel = models.BooleanField(
        blank=True, default=False
    )
    social_community_rel = models.BooleanField(
        blank=True, default=False
    )
    social_peace_advocacy = models.BooleanField(
        blank=True, default=False
    )

    competency_comm = models.BooleanField(
        blank=True, default=False
    )
    competency_analytical = models.BooleanField(
        blank=True, default=False
    )
    competency_entrepreneurial = models.BooleanField(
        blank=True, default=False
    )
    competency_research = models.BooleanField(
        blank=True, default=False
    )
    competency_math = models.BooleanField(
        blank=True, default=False
    )
    competency_leadership = models.BooleanField(
        blank=True, default=False
    )
    competency_human_rel = models.BooleanField(
        blank=True, default=False
    )
    competency_cit = models.BooleanField(
        blank=True, default=False
    )
    competency_learning_efficiency = models.BooleanField(
        blank=True, default=False
    )

    other_ndu_alumni = models.TextField(blank=True, default='')

    def __str__(self):
        return f'{self.user.username}'
