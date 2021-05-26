from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def my_post(request):
    return render(request, 'myPost.html')