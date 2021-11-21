from django.shortcuts import render
from django.utils import timezone
from .models import Plan

# Create your views here.


def plan_list(request):
    plans = Plan.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'merchandise/plan_list.html', {'plans': plans})
