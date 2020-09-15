from django.shortcuts import render
import requests


def my_list(request):
    url = 'http://www.omdbapi.com/?apikey=704eb2&s=jumanji'
    response = requests.get(url).json()
    context = {
        'response' : response
    }
    return render(request,'movies.html',context)
