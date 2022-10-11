from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard),
    path("search/", views.search),
    path("search_result/", views.search_result),
    path("car_select/", views.car_select),
    path("car_details/", views.car_details),
    path("car_book/", views.car_book),
    path("login/", views.login),
    path("register/", views.register),
    path("customer_register/", views.customer_register),
    path("provider_register/", views.provider_register),
    path("payment_method/", views.payment_method),
    path("payment_confirmation/", views.payment_confirmation),
    path("confirm_book/", views.confirm_book),
    path("provider_dashboard/", views.provider_dashboard),
    path("add_edit/", views.add_edit),
    path("insert_car/", views.insert_car),
    path("delete/", views.delete),
]
