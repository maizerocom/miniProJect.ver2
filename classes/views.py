from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from classes.models import Restaurant, Faculty
# Create your views here.
def index(request):
    search_txt = request.GET.get('inputSearch', '')

    faculty = Faculty.objects.all()
    classes = Restaurant.objects.filter(
        name__icontains=search_txt
    )
    return render(request, 'classes/index.html', context={
        'search_txt': search_txt,
        'classes': classes,
        'faculty': faculty
    })