from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings

def index(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def send_email(request):
    subject = "You Might be Interested in This Product"
    message = "Hello, Check this out!"
    from_email = settings.EMAIL_HOST_USER
    
    recipient_list = ["ammarasim065@gmail.com"]
    try:
        send_mail(subject, message, from_email, recipient_list,)
    except BadHeaderError:
        return HttpResponse('Invalid header found.')    
    return render(request, 'core/about.html') 