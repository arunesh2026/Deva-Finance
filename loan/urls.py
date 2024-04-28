from django.urls import path

from loan.views import loan_application, subscription, free_subscription, paid_subscription


urlpatterns = [
    path("apply-loan/", view=loan_application, name="loan_application"),
    path("subscription/", view=subscription, name="subscription"),
    path("free-package/", view=free_subscription, name="free_subscription"),
    path("paid-package/", view=paid_subscription, name="paid_subscription"),
]
