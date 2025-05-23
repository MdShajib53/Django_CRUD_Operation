from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse("This is Simple Website")


def index(request):
    return render(request, 'index.html')