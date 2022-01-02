from django.shortcuts import render


def home(request):
    # main page
    return render(request, 'index.html')
