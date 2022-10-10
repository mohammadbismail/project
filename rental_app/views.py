from django.shortcuts import render, redirect
from .models import Customer, Car, Provider, Feedback


def register_page(request):
    context = {
        "all_cars": Car.objects.all(),
    }
    return render(request, "customer/search.html", context)


