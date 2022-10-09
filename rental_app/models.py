from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    mobile = models.IntegerField()
    age = models.IntegerField()
    national_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# each user can be a customer optionally if he booked a car
class Customer(models.Model):
    user = models.OneToOneField(User, primary_key=True,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # cars_booked


class Provider(models.Model):
    name = models.CharField(max_length=50)
    permit = models.IntegerField()
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # cars_provided
    # customer_feedbacks


# car can be booked by many customers at different times, while
# customer can book many cars at once
class Car(models.Model):
    customers = models.ManyToManyField(Customer, related_name="cars_booked")
    provider = models.ForeignKey(Provider, related_name="cars_provided",on_delete=models.CASCADE)
    brand = models.CharField(max_length=45)
    model = models.CharField(max_length=45)
    plate_number = models.CharField(max_length=45)
    production_year = models.IntegerField()
    engine = models.IntegerField()
    pickup_date = models.DateTimeField(
        null=True
    )  # this field can be empty unless while creating car, unless its booked
    drop_date = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # feedbacked_cars


# car can have multiple feedbacks - a feedback can be for mutiple cars

class Feedback(models.Model):
    details = models.TextField(null=True)
    customer = models.ForeignKey(Customer, related_name="customer_feedbacks",on_delete=models.CASCADE)
    rating = models.IntegerField()
    cars = models.ManyToManyField(Car, related_name="feededbacked_cars")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
