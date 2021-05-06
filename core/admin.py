from django.contrib import admin
from .models import GeneralContact, JoinContact, JobContact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date_created')

admin.site.register(GeneralContact, ContactAdmin)
admin.site.register(JoinContact, ContactAdmin)
admin.site.register(JobContact, ContactAdmin)
