from django.urls import path

from student.views import student_loan, subscription_student_loan


urlpatterns = [
    path("loan-application/", view=student_loan, name="student_loan"),
    path("subscription/", view=subscription_student_loan, name="subscription_student_loan"),
]
