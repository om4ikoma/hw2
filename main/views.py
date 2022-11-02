from django.shortcuts import render, redirect
from datetime import datetime

from main.forms import DirectorForm, FilmForm
from main.models import Film, Director


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


def films_list_view(request):
    context = {}
    context['films'] = Film.objects.all()
    return render(request, 'films_list.html', context=context)


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
