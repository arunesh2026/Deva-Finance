from django.contrib import admin

from loan.models import LoanApplication


@admin.register(LoanApplication)
class LoanApplicationAdmin(admin.ModelAdmin):
    list_display = ["id", "application_number", "full_name", "mobile", "payment_done", "called", "created_date"]
    list_display_links =  ["id", "application_number", "full_name", "mobile"]
    readonly_fields = ["application_number"]
    search_fields = ["application_number", "full_name", "mobile", "email"]
    list_filter = ["payment_done", "called"]