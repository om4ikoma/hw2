from django.shortcuts import render
from datetime import datetime
from main.models import Film


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