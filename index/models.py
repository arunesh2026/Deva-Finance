from django.db import models


class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    send_date = models.DateTimeField(auto_now_add=True)
    checked = models.BooleanField(default=False, blank=True)