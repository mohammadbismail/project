from django.db import models


# Relation no.1
# Customer-Car (Many-->Many) car can be booked by many customers at different times
# while customer can book many cars as he desires
# ---------------------------------------------------------------------------------
# Relation no.2
# Customer-Feedback (One-->Many) customer can give many feedback on cars he booked
# while a feedback is related is coming from single customer
# ----------------------------------------------------------------------------------
# Relation no.3
# Provider-Car (One-->Many) provider can provide group of cars while car has to come from single provider
# ----------------------------------------------------------------------------------
# Relation no.4
# Car-Feedback (Many-->Many) car can have many feedbacks & feedback can be more many cars


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    mobile = models.IntegerField()
    age = models.IntegerField()
    national_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # cars_booked
    # customer_feedbacks


class Provider(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    mobile = models.IntegerField()
    permit = models.IntegerField()
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # cars_provided


class Car(models.Model):
    customers = models.ManyToManyField(Customer, related_name="cars_booked")
    provider = models.ForeignKey(Provider, related_name="cars_provided", on_delete=models.CASCADE)
    brand = models.CharField(max_length=45)
    model = models.CharField(max_length=45)
    plate_number = models.CharField(max_length=45)
    production_year = models.IntegerField()
    engine = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # feedbacked_cars


class Feedback(models.Model):
    details = models.TextField(null=True)
    customer = models.ForeignKey(
        Customer, related_name="customer_feedbacks", on_delete=models.CASCADE
    )
    rating = models.IntegerField()
    cars = models.ManyToManyField(Car, related_name="feededbacked_cars")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
