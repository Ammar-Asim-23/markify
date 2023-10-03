from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from lead.models import Lead
from client.models import Client
from team.models import Team
from product.models import Product, Advertisement


@login_required
def dashboard(request):
    team = Team.objects.filter(created_by=request.user)[0]
    leads = Lead.objects.filter(team = team, converted_to_client=False).order_by('-created_at')[:5]
    clients = Client.objects.filter(team = team).order_by('-created_at')[:5]
    products = Product.objects.filter(team = team).order_by('-created_at')[:5]
    ads = Advertisement.objects.order_by('-activity')[:5]
    return render(request, 'dashboard/dashboard.html',{
        'clients':clients,
        'leads':leads,
        'products':products,
        'ads':ads,
    })
