from django.shortcuts import render, redirect


# Create your views here.


def login_page(request):
    return render(request, '../templates/login.html')


def redirect_to_telegram(request):
    return redirect("https://google.com")
