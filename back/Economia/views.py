
from django.http import JsonResponse
from .models import EconomicIndicator

def economic_indicators(request):
    data = {
        indicator.name: indicator.value
        for indicator in EconomicIndicator.objects.all()
    }
    return JsonResponse(data)