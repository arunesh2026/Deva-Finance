from django.shortcuts import render, redirect

from student.forms import StudentLoanForm


def student_loan(request):
    
    if request.method == "POST":
        loan_form = StudentLoanForm(request.POST)
        
        if loan_form.is_valid():
            loan_form.save()
            
        return redirect("subscription_student_loan")
    
    context = {
        "form": StudentLoanForm()
    }
    
    return render(request=request, template_name="student/student-loan-application.html", context=context)


def subscription_student_loan(request):
    return render(request=request, template_name="student/subscription-student-loan.html")