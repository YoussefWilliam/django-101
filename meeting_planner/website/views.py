from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def welcome(request):
    return HttpResponse("Welcome to the meeting planner!")

def date(request):
    return HttpResponse('This is the date of that moment' + " " + str(datetime.now()))


def info(request):
    return HttpResponse("My name is youssef, and i live in Egypt")
