from django import forms

from loan.models import LoanApplication



class LoanForm(forms.ModelForm):
    class Meta:
        model = LoanApplication
        
        fields = ["full_name",
                "mobile",
                "email",
                "address",
                "employment_type",
                "require_amount",
                "monthly_income",
                "loan_purpose",
                "loan_type",
            ]
        
        labels = {
            "full_name": "Full Name",
            "mobile": "Contact Number",
            "email": "Email Address",
            "address": "Full Address",
            "employment_type": "Employment Type",
            "require_amount": "Require Amount",
            "monthly_income": "Monthly Income",
            "loan_purpose": "Loan Purpose",
            "loan_type": "Loan Type",
        }
        
        widgets = {
            "full_name": forms.TextInput(attrs={"class": "form-control bg-white mb-4"}),
            "email": forms.EmailInput(attrs={"class": "form-control bg-white mb-4"}),
            "mobile": forms.NumberInput(attrs={"class": "form-control bg-white mb-4"}),
            "address": forms.TextInput(attrs={"class": "form-control bg-white mb-4"}),
            "require_amount": forms.NumberInput(attrs={"class": "form-control bg-white mb-4"}),
            "monthly_income": forms.NumberInput(attrs={"class": "form-control bg-white mb-4"}),
            
            "employment_type": forms.Select(attrs={"class": "form-control w-100 bg-white mb-4"}),
            "loan_purpose": forms.Select(attrs={"class": "form-control w-100 bg-white mb-4"}),
            "loan_type": forms.Select(attrs={"class": "form-control w-100 bg-white mb-4"}),
        }
