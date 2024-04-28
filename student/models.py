from django.db import models


import random
import string

def generate_custom_id():
    random_chars = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    return f"{random_chars}"


GENDER_CHOICES = {
    "male": "Male",
    "female": "Female",
    "other": "Other"
}


class StudentLoan(models.Model):
    require_amount = models.IntegerField()
    full_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(max_length=255)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255)
    
    school_name = models.CharField(max_length=255)
    
    application_number = models.CharField(max_length=10, default=generate_custom_id)
    
    payment_amount = models.IntegerField(blank=True, null=True)
    payment_done = models.BooleanField(default=False)
    called = models.BooleanField(default=False, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)