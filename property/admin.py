from django.contrib import admin

from .models import Flat, AdminFeature, Complaint


admin.site.register(Flat,AdminFeature)
admin.site.register(Complaint)
