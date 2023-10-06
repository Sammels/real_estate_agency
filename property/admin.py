from django.contrib import admin

from .models import Flat, AdminFeature


admin.site.register(Flat, AdminFeature)
