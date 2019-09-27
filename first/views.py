from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def connect(request):
    return render(request, 'connect.html')

def resume(request):
    return render(request, 'resume.html')