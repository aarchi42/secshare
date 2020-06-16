from django.contrib import admin
from django.contrib.sites.models import Site
from .models import Verification, Images

admin.site.register(Verification)
admin.site.register(Images)

admin.site.unregister(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'domain', 'name')

admin.site.register(Site, SiteAdmin)