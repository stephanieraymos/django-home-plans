from django.shortcuts import render
from .models import OutdoorPlan

def home(request):
    outdoorPlans = OutdoorPlan.objects
    return render(request, 'outdoorPlans/home.html', {'outdoorPlans': outdoorPlans})

def detail(request, outdoorPlan_id):
    print(outdoorPlan_id)
    return render(request, 'outdoorPlans/home.html')