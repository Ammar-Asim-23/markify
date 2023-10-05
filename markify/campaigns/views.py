from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from .models import Campaign
from client.models import Client
from product.models import Advertisement



def campaigns_list(request):
    campaigns = Campaign.objects.filter(active=True)
    return render(request, 'campaigns/campaign_list.html', {'campaigns': campaigns})

def send_email(request, pk):
    campaign = Campaign.objects.filter(active=True).get(pk=pk)
    if campaign is None:
        return HttpResponse('Invalid campaign')
    clients = Client.objects.all()
    ads = Advertisement.objects.filter(campaign=campaign).order_by('-activity')
    if len(ads) == 0:
        messages.success(request, 'No advertisement found for this campaign')
        return redirect('campaigns:list')
    
    ad = ads[0]
    subject = "From Markify: " + campaign.title
    message = ad.description + "\nFor more information visit our website"
    
    from_email = settings.EMAIL_HOST_USER
    
    client_emails = [client.email for client in clients]

    try:
        send_mail(subject, message, from_email, client_emails,)
    except BadHeaderError:
        return HttpResponse('Invalid header found.')    
    messages.success(request, 'The client has recieved your campaign emails.')
    return redirect('campaigns:list')

