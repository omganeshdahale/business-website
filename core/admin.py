from django.contrib import admin
from .models import GeneralContact, JoinContact, JobContact

admin.site.register(GeneralContact)
admin.site.register(JoinContact)
admin.site.register(JobContact)
