from django.shortcuts import render, redirect
from .models import Customer, Car, Provider, Feedback


def register_page(request):
    context = {
        "all_cars": Car.objects.all(),
    }
    print(context["all_cars"])
    return render(request, "customer/search.html", context)
