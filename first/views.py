from django.shortcuts import render
from first import models, forms
from first.models import SignForm
from first.forms import SignUp


# Create your views here.
def index(request):
    return render(request, 'index.html')

def connect(request):
    return render(request, 'connect.html')

def resume(request):
    return render(request, 'resume.html')

def guest(request):
    form = SignUp()

    if request.method == "POST":
        form = SignUp(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR! FORM INVALID")

    return render(request, "guest.html", {'sign_form': form})

def user(request):
    user_list = SignForm.objects.order_by('last')
    return render(request, 'book.html', {'user': user_list})