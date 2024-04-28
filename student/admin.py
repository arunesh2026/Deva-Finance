from django.contrib import admin

from student.models import StudentLoan


@admin.register(StudentLoan)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "application_number", "full_name", "payment_done", "called", "created_date"]
    list_display_links = ["id", "full_name", "application_number"]
    search_fields = ["application_number", "full_name", "mobile", "email"]
    list_filter = ["payment_done", "called"]
    readonly_fields = ["application_number"]