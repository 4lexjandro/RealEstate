
# cusstomize admin stuff for listings app here
from django.contrib import admin
from .models import Listing#check class for 'Listing' from models.py file

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_publichsed', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_publichsed',)
    search_fields = ('title', 'description', 'address', 'city', 'state', 'price',)
    list_per_page = 25




admin.site.register(Listing, ListingAdmin)
