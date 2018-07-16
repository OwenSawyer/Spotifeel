# views.py
from django.http import JsonResponse
from django.shortcuts import HttpResponse
from rest_framework.decorators import api_view

@api_view(['GET'])
def index(request):
    return JsonResponse({"text": "Hello World"})

def response_handler(response):
    if 'status' in response:
        return HttpResponse(reason=response['status'], status=response['status']['status_code'])
    if isinstance(response, list) and not response:
        return HttpResponse(reason="No data available", status=400)
    return JsonResponse(response)
