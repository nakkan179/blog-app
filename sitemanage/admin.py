from django.contrib import admin
from .models import SiteConfig
from django.contrib.sites.models import Site

@admin.register(SiteConfig)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'meta_title',)
    list_display_links = ('meta_title',)
