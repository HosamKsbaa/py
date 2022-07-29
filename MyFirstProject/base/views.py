from multiprocessing import context
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.




room =[
    {'id':1,"name":"room1"}, {'id':2,"name":"room2"}, {'id':3,"name":"room3"}, {'id':4,"name":"room4"}
]
def home(request):
    context = {'room': room}
    return render(request, 'base/home.html',context)


def room(request):
    return render(request, 'base/room.html')
