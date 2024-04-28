from django.shortcuts import render, redirect

from index.forms import ContactForm


def home(request):
    return render(request=request, template_name="index/index.html")


def about(request):
    return render(request=request, template_name="index/about.html")


def contact(request):
    contact_form = ContactForm()
    
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        
        if contact_form.is_valid():
            contact_form.save()
            
            return redirect("contact_success")
    
    context = {
        "contact_form": contact_form
    }    
    
    return render(request=request, template_name="index/contact.html", context=context)


def contact_success(request):
    return render(request=request, template_name="index/contact-success.html")



def emi_calculator(request):
    return render(request=request, template_name="index/emi-calculator.html")



def services(request):
    return render(request=request, template_name="index/services.html")



def privacy_policy(request):
    return render(request=request, template_name="index/privacy-policy.html")


def safety_guide(request):
    return render(request=request, template_name="index/safety-guide.html")


def faq_view(request):    
    return render(request=request, template_name="index/faq.html")