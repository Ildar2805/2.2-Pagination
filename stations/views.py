from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from pagination.settings import BUS_STATION_CSV
import csv


with open(BUS_STATION_CSV, encoding='utf8') as file:
    reader = csv.DictReader(file)
    need_list = list(reader)


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(need_list, 10)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
