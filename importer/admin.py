from django.contrib import admin
from .models import CsvJobs, Contacts


class JobsAdmin(admin.ModelAdmin):
    list_display = ('job_id',)


class ContactsAdmin(admin.ModelAdmin):
    list_display = ('Name',)


admin.site.register(CsvJobs, JobsAdmin)
admin.site.register(Contacts, ContactsAdmin)
