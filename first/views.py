from django.shortcuts import render
from first import models, forms
from first.models import SignForm, Article
from first.forms import SignUp, MovieForm
from first.api import Imdb

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
            return user(request)
        else:
            print("ERROR! FORM INVALID")

    return render(request, "guest.html", {'sign_form': form})

def user(request):
    user_list = SignForm.objects.order_by('last')
    return render(request, 'book.html', {'user': user_list})

def movie(request):
    mform = MovieForm()

    if request.method == "POST":
        mform = MovieForm(request.POST)

        if mform.is_valid():
            temp = mform.cleaned_data['title']
            return search(request, temp)
        else:
            print("ERROR! FORM INVALID")

    return render(request, "movie.html", {'movie_form': mform})

def search(request, mform):
    movie_list = Imdb()
    search = movie_list.query(mform)
    if search['Response'] == 'True':
        return render(request, 'search.html', {'movie': search['Search']})
    else:
        return render(request, 'error.html', {'movie': search})
    
def blog(request):
    articles = Article.objects.all().order_by('-date')
    return render(request, 'blog.html', {'artical' : articles})

