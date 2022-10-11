from django.shortcuts import render, redirect
from .models import Customer, Provider, Car
import bcrypt
from django.contrib import messages


def dashboard(request):
    return render(request, "dashboard.html")


def search(request):
    return redirect("/search_result")


def search_result(request):
    return render(request, "search_result.html")


def car_select(request):
    return redirect("/car_details")


def car_details(request):
    return render(request, "car_details.html")


def car_book(request):
    return redirect("/payment_confirmation")


def login(request):

    errors = Customer.objects.customer_login_validator(request.POST)
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect("/")

    errors = Provider.objects.provider_login_validator(request.POST)
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect("/")

    customer = Customer.objects.filter(email=request.POST["email"])
    if customer:
        logged_customer = customer[0]
        if bcrypt.checkpw(
            request.POST["password"].encode(), logged_customer.password.encode()
        ):
            request.session["customer_id"] = logged_customer.id
            request.session["customer_first_name"] = logged_customer.first_name

        return redirect("/")

    provider = Provider.objects.filter(email=request.POST["email"])
    if provider:
        logged_provider = provider[0]
        if bcrypt.checkpw(
            request.POST["password"].encode(), logged_provider.password.encode()
        ):
            request.session["provider_id"] = logged_provider.id
            request.session["provider_name"] = logged_provider.name

        return redirect("/provider_dashboard")


def register(request):
    return render(request, "register.html")


def customer_register(request):

    errors = Customer.objects.customer_validator(request.POST)
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect("/register/")

    password = request.POST["password"]
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    Customer.objects.create(
        first_name=request.POST["firstName"],
        last_name=request.POST["lastName"],
        email=request.POST["email"],
        password=pw_hash,
        mobile=request.POST["mobile"],
        birthday=request.POST["birthday"],
        national_id=request.POST["national_id"],
    )
    return redirect("/")


def provider_register(request):

    errors = Provider.objects.provider_validator(request.POST)
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect("/register/")

    password_from_form = request.POST["password"]
    pw_hash = bcrypt.hashpw(password_from_form.encode(), bcrypt.gensalt()).decode()

    Provider.objects.create(
        name=request.POST["name"],
        email=request.POST["email"],
        password=pw_hash,
        mobile=request.POST["mobile"],
        permit=request.POST["permit"],
        location=request.POST["location"],
    )
    return redirect("/provider_dashboard")


def payment_method(request):
    return render(request, "payment_method.html")


def payment_confirmation(request):
    return render(request, "payment_confirmation.html")


def confirm_book(request):
    return redirect("/")


def provider_dashboard(request):
    return render(request, "provider_dashboard.html")


def add_edit(request):
    return render(request, "add_edit.html")


def insert_car(request):

    Car.objects.create(
        brand=request.POST["brand"],
        model=request.POST["model"],
        production_year=request.POST["production_year"],
        plate_number=request.POST["plate_number"],
        provider=Provider.objects.get(id=request.session["provider_id"]),
    )
    return redirect("/add_edit")


def delete(request):

    del request.session["customer_id"]
    del request.session["provider_id"]
    del request.session["customer_first_name"]
    del request.session["provider_name"]

    return redirect("/")
