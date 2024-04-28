from django.urls import path

from index.views import home, about, contact, emi_calculator, services, privacy_policy, safety_guide, contact_success, faq_view


urlpatterns = [
    path("", view=home, name="home"),
    path("about/", view=about, name="about"),
    path("contact/", view=contact, name="contact_us"),
    path("contact-send-success/", view=contact_success, name="contact_success"),
    path("emi-calculator/", view=emi_calculator, name="emi_calculator"),
    path("services/", view=services, name="services"),
    path("privacy-policy/", view=privacy_policy, name="privacy_policy"),
    path("safety-guide/", view=safety_guide, name="safety_guide"),
    path("loan-faq/", view=faq_view, name="faq_view"),
]
