from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Hello, World</h1>')


def search(request, keyword, page):
    return HttpResponse(f'<h1>Search for: {keyword}, Page: {page}</h1>')


def date(request, day, month, year):
    return HttpResponse(f'<h1>Date: {day} - {month} - {year}</h1>')


def redirect(request, url):
    return HttpResponse(f'<a href="{url}" target="_blank">Click here to redirect</a>')


def article(request, id, title):
    return HttpResponse(f'<h1>Article ID: {id} Title: {title}')


# http://localhost:8000/map/?type=satellite&lat=13.34&log=12.34&zoom=1
def map(request):
    print('request:', request)

    type = request.GET.get('type')
    lat = request.GET.get('lat')
    log = request.GET.get('log')
    zoom = request.GET.get('zoom')

    return HttpResponse(f'<h1>Type: {type}, Lat: {lat}, Log: {log} and Zoom: {zoom}.</h1>')
