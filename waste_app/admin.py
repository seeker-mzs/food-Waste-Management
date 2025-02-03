from django.contrib import admin
from .models import Donation, WasteTracking, Request

admin.site.register(Donation)
admin.site.register(WasteTracking)
admin.site.register(Request)
