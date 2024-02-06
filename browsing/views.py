from contextlib import redirect_stderr
from http.client import HTTPResponse
from .models import Movie, Reserve
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.conf.urls.static import static
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import CreateUserForm

# Create your views here.

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for '+ user)

                return redirect('/login')
        context = {
            'form':form,
        }
        return render(request, 'browsing/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')

                user = authenticate(username=username, password=password)
        
                if user is not None:
                    login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
        form = AuthenticationForm()   
        
        return render(request=request, template_name="browsing/login.html", context={"login_form":form})

def logoutUser(request):
    logout(request)
    return redirect('/login')


def home(request):
    movies = Movie.objects.all()
    reserves = Reserve.objects.all()
    context = {
        'movies':movies,
        'reserves':reserves,
    }
    return render(request, 'browsing/index.html', context)


def movies(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'browsing/Movies.html', context)

@login_required(login_url='/login')
def moviesbooking(request, id):
    movie = Movie.objects.get(id=id)
    context = {
        'movie':movie,
    }
    if request.method == 'POST':
        movie.quantity = request.POST.get('quantity')
        movie.save()
    return render(request, 'browsing/Movies.html', context)

@login_required(login_url='/login')
def reserves(request):
    reserves = Reserve.objects.all()
    context = {
        'reserves': reserves,
    }
    return render(request, 'browsing/Movies.html', context)

@login_required(login_url='/login')
def reservedetails(request, id):
    reserve = Reserve.objects.get(id=id)
    context = {
        'reserve':reserve,
    }
    if request.method == 'POST':
        reserve.quantity = request.POST.get('quantity')
        reserve.save()
    return render(request, 'browsing/Reserve.html', context)

def privacy(request):
    return render(request, 'partials/Privacy.html')

def terms(request):
    return render(request, 'partials/TermsService.html')

def about(request):
    return render(request, 'partials/About.html')

def faq(request):
    return render(request, 'partials/FAQ.html')

def services(request):
    return render(request, 'partials/Services.html')

def searchBar(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        if query:
            movies = Movie.objects.filter(title__contains=query)
            reserves = Reserve.objects.filter(title__contains=query)
            return render(request, 'partials/search.html', { 'movies':movies,'reserves':reserves })
        else:
            print("Nothing to show....")
            return render(request, 'partials/search.html', {})


    
