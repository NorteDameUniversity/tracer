from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, DetailView, UpdateView, CreateView

from . import models, forms


class IndexView(TemplateView):
    template_name = 'profiles/index.html'


class ProfileView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        profile, _ = models.Profile.objects.get_or_create(
            defaults={'user': request.user},
            user=request.user)
        return redirect(reverse('profile-detail', kwargs={'pk': profile.pk}))


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = models.Profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        rows = (
            ('Full Name', self.object.full_name),
            ('Student number', self.object.student_number),
            ('Degree/Course', self.object.degree),
            ('Specialization/Major', self.object.specialization),
            ('Year graduated from Notre Dame University',
             self.object.year_graduated_ndu),
            # ('Last name', self.object.last_name),
            # ('First name', self.object.first_name),
            # ('Middle name', self.object.middle_name),
            # ('Name extension', self.object.name_ext),
            ('Mailing Address (Blk No., Lot No. Street, Subd., Brgy, City/Municipality, Province, Country)', self.object.address),
            ('Birthdate (mm/dd/yyyy, eg. 08/02/1976)', self.object.birthdate),
            ('Gender', self.object.get_gender_display()),
            ('Civil Status', self.object.get_civil_status_display()),
            ('Preferred Mailing Address',
             self.object.preferred_mailing_address),
            ('Alternate email', self.object.alternate_email),
            ('Contact Number/s', self.object.contact_numbers),
            ('Is National Licensure Exam Passer',
             self.object.is_natl_lic_exam_passer),
            ('Field of Examination Passed',
             self.object.get_field_exam_passed_display()),
            ('Year Passed the Licensure Exam',
             self.object.field_exam_year_passed),

        )

        is_survey_completed = models.Survey.objects.filter(
            user=self.object.user
        ).exists()
        context.update({
            'profile_table_rows': rows,
            'is_survey_completed': is_survey_completed
        })
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Profile
    form_class = forms.ProfileForm

    def form_valid(self, form):
        messages.success(self.request, 'Profile was updated.')
        return super().form_valid(form)

class SurveyCreateView(LoginRequiredMixin, CreateView):
    model = models.Survey
    form_class = forms.SurveyForm

    def get_initial(self):
        return {
            'user': self.request.user
        }

    def get_success_url(self):
        return reverse('index')

    def form_valid(self, form):
        messages.success(self.request, 'Suvey was completed.')
        return super().form_valid(form)
