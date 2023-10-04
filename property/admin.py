from django.contrib import admin

from .models import Flat, SearchLine


admin.site.register(Flat, SearchLine)
