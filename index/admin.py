from django.contrib import admin

from index.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["id", "full_name", "phone", "email", "subject", "send_date", "checked"]
    
    list_display_links = ["id", "full_name"]