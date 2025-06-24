from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import DailyStats

def dashboard(request):
    stats = DailyStats.objects.order_by('date')
    dates = [stat.date.strftime('%Y-%m-%d') for stat in stats]
    sowings = [stat.total_sowings for stat in stats]
    soil_analyses = [stat.total_soil_analyses for stat in stats]

    context = {
        'dates': dates,
        'sowings': sowings,
        'soil_analyses': soil_analyses,
    }
    return render(request, 'estadistica/dashboard.html', context)
