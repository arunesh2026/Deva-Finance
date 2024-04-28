from django.urls import path

from dashboard.views import register, login_view, logout_view, dashboard, applied_loan


urlpatterns = [
    path("sign-up/", view=register, name="register"),
    path("login/", view=login_view, name="login"),
    path("logout/", view=logout_view, name="logout"),
    path("dashboard/", view=dashboard, name="dashboard"),
    path("applied-loan/", view=applied_loan, name="applied_loan"),
]
