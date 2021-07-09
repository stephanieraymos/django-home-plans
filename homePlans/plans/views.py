from django.shortcuts import render, get_object_or_404
from .models import Plan

def home(request):
    plans = Plan.objects
    return render(request, 'plans/home.html', {'plans': plans})

def detail(request, plan_id):
    plan_detail = get_object_or_404(Plan, pk=plan_id)
    return render(request, 'plans/home.html')