from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def neindex(request):
    return render(request, 'neindex.html')

