from django.contrib import admin
from .models import Contact


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'subject', 'message', 'date',)
    list_filter = ('email',)
    search_fields = ('email',)
    date_hierarchy = 'date'


admin.site.register(Contact, ContactAdmin)
