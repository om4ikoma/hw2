from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from datetime import datetime
from main.forms import DirectorForm, FilmForm, UserCreateForm, UserLoginForm
from main.models import Film, Director
from django.views.generic import ListView


def about_us(request):
    return render(request, "about_us.html")


def date_now(request):
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day
    return render(request, 'datetime_now.html', context={
        'year': year,
        'month': month,
        'day': day
    })




def film_view(request, id):
    context = {}
    context['film'] = Film.objects.get(id=id)
    return render(request, 'film.html', context=context)


def director_films(request, director_id):
    director = Director.objects.get(id=director_id)
    films = Film.objects.filter(director_id=director)
    context = {}
    context['films_director'] = films
    context['director'] = director
    return render(request, 'director_films.html', context=context)


def create_director(request):
    if request.method == "POST":
        form = DirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'create_director.html', context={
        'form': DirectorForm()
    })


def create_film(request):
    if request.method == "POST":
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'create_film.html', context={
        'form': FilmForm()
    })


def register(request):
    context = {
        'form': UserCreateForm(request.POST)
    }
    if request.method == 'POST':
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            User.objects.create_user(username=username, password=password)
            return redirect('/films/')
        context['form'] = form
    return render(request, 'register.html', context=context)


def login_view(request):
    context = {
        'form': UserLoginForm()
    }
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('/films/')
            else:
                return redirect('/login/')
    return render(request, 'login.html', context=context)


class FilmsSearchView(ListView):
    queryset = Film.objects.all()
    template_name = 'search.html'
    context_object_name = 'films'

    def get_query_set(self):
        search_word = self.request.GET.get('search_word', '')
        return self.queryset.filter(title__icontains=search_word)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_word'] = self.request.GET.get('search_word', '')
        context['films'] = Film.objects.all()
        return context


def search(request):
    search_word = request.GET.get('search_word', '')
    context = {
        'films': Film.objects.filter(title__icontains=search_word),
        'search_word': search_word,
    }
    return render(request, 'search.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('/')


PAGE_SIZE = 3


def films_list_view(request):
    page = int(request.GET.get('page', 1))
    all_films = Film.objects.all()
    films = all_films[(page - 1) * PAGE_SIZE: page * PAGE_SIZE]
    pages = (all_films.count() + PAGE_SIZE - 1) // PAGE_SIZE
    data = {
        'films': films,
        'buttons': [i for i in range(1, pages + 1)],
        'prev_page': page - 1,
        'next_page': page + 1,
        'page': page,
        'pages': pages,
    }
    return render(request, 'films_list.html', data)
