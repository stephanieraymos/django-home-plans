from django.shortcuts import render
from .models import OutdoorPlan

def home(request):
    outdoorPlans = OutdoorPlan.objects
    return render(request, 'outdoorPlans/home.html', {'outdoorPlans': outdoorPlans})
