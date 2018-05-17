from django.contrib import admin

from . import models


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Survey)
class SurveyAdmin(admin.ModelAdmin):
    pass
