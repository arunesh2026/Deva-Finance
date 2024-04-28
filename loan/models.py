from django.db import models

import random
import string

def generate_custom_id():
    random_chars = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    return f"{random_chars}"


LOAN_PURPOSE_CHOICES = {
    "Personal Use": "Personal Use",
    "Business Expansion": "Business Expansion",
    "Maintain Cash Flow": "Maintain Cash Flow",
    "Property Renovation": "Property Renovation",
    "Marriage Purpose": "Marriage Purpose",
    "Education Purpose": "Education Purpose",
    "Medical Emergency": "Medical Emergency",
    "Other": "Other"
}


LOAN_TYPE_CHOICES = {
    "Personal Loan": "Personal Loan",
    "Home Loan": "Home Loan",
    "Gold Loan": "Gold Loan",
    "Business Loan": "Business Loan",
    "Agriculture Loan": "Agriculture Loan",
    "Vehicle Loan": "Vehicle Loan",
    "Education Loan": "Education Loan",
    "Loan Against Property": "Loan Against Property",
}

EMPLOYMENT_TYPE_CHOICES = {
    "Salaried": "Salaried",
    "Self-Employed": "Self-Employed",
}

class LoanApplication(models.Model):
    require_amount = models.IntegerField()
    full_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=13)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=355)
    employment_type = models.CharField(max_length=50, choices=EMPLOYMENT_TYPE_CHOICES)
    
    monthly_income = models.IntegerField()
    
    loan_purpose = models.CharField(max_length=100, choices=LOAN_PURPOSE_CHOICES, default="Personal Use")
    loan_type = models.CharField(max_length=100, choices=LOAN_TYPE_CHOICES, default="Personal Loan")
    
    payment_amount = models.CharField(max_length=50, blank=True)
    payment_done = models.BooleanField(default=False, blank=True)
    
    application_number = models.CharField(max_length=10, default=generate_custom_id)
    
    called = models.BooleanField(default=False, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)