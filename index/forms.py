from django import forms

from index.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["full_name", "email", "phone", "subject", "message"]
        
        labels = {
            "full_name": "Full Name",
            "email": "Email Address",
            "phone": "Contact Number",
        }
        
        widgets = {
            "full_name": forms.TextInput(attrs={"class": "form-control mb-4"}),
            "email": forms.EmailInput(attrs={"class": "form-control mb-4"}),
            "phone": forms.TextInput(attrs={"class": "form-control mb-4"}),
            "subject": forms.TextInput(attrs={"class": "form-control mb-4"}),
            "message": forms.Textarea(attrs={"class": "border w-100 p-3 mb-4"}),
        }
        