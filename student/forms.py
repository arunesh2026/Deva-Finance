from django import forms

from student.models import StudentLoan


class DateInput(forms.DateInput):
    input_type = 'date'


class StudentLoanForm(forms.ModelForm):
    # date_of_birth = forms.DateField(widget=forms.DateInput())

    
    class Meta:
        model = StudentLoan
        
        fields = [
                "require_amount",
                "full_name",
                "mobile",
                "email",
                "address",
                "gender",
                "date_of_birth",
                "school_name",
            ]
        
        labels = {
            "full_name": "Full Name",
            "mobile": "Contact Number",
            "email": "Email Address",
            "address": "Current Address",
            "gender": "Gender",
            "date_of_birth": "Date Of Birth",
            "school_name": "School Name",
            "require_amount": "Enter Loan Amount",
        }
        
        widgets = {
            "full_name": forms.TextInput(attrs={"class": "form-control bg-white mb-4"}),
            "email": forms.EmailInput(attrs={"class": "form-control bg-white mb-4"}),
            "mobile": forms.NumberInput(attrs={"class": "form-control bg-white mb-4"}),
            "require_amount": forms.NumberInput(attrs={"class": "form-control bg-white mb-4"}),
            "address": forms.TextInput(attrs={"class": "form-control bg-white mb-4"}),
            "school_name": forms.TextInput(attrs={"class": "form-control bg-white mb-4"}),
            "gender": forms.Select(attrs={"class": "form-control w-100 bg-white mb-4"}),
            
            'date_of_birth': DateInput(attrs={"class": "form-control w-100 bg-white mb-4"}),
        }
