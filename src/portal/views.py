from django.shortcuts import render


def home(request):
    """
    Home
    """
    return render(request, "portal/home.html")
