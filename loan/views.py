from django.shortcuts import render, redirect

from loan.forms import LoanForm


def loan_application(request):
    
    if request.method == "POST":
        loan_form = LoanForm(request.POST)
        
        if loan_form.is_valid():
            loan_form.save()
            
        return redirect("subscription")
        
    context = {
        "loan_form": LoanForm()
    }
        
    
    return render(request=request, template_name="loan/loan-application.html", context=context)



def subscription(request):
    return render(request=request, template_name="loan/subscription.html")


def free_subscription(request):
    return render(request=request, template_name="loan/free-subscription.html")


def paid_subscription(request):
    return render(request=request, template_name="loan/paid-subscription.html")