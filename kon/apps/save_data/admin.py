from django.contrib import admin
from .models import *

@admin.register(Base_Information)
class BaseInformationAdmin(admin.ModelAdmin):
    readonly_fields = ('sub_AS', 'execut_full_name', 'person_file_location')
    fields = ('sub_AS', 'execut_full_name', 'person_file_location')
    list_display = ('sub_AS', 'execut_full_name', 'file_location')

    def person_file_location(self, obj):
        return obj.file_location()

