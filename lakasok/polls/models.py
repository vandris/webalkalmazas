from django.db import models

class Users(models.Model):
    email = models.CharField(max_length=200, unique=True)
    fullname = models.CharField(max_length=200)
    password = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    age = models.IntegerField(default=40)
    valid = models.BooleanField(default=True)

    def __str__(self):
        return self.email

class Adds(models.Model):
    owner = models.CharField(max_length=200)
    squaremeter = models.IntegerField(default=40)
    price = models.IntegerField(default=10000)
    type = models.CharField(max_length=50)
    wall = models.CharField(max_length=50)
    heating = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    rooms = models.IntegerField(default=3)
    parking = models.CharField(max_length=100)
    year = models.IntegerField(default=2017)
    furnitured = models.BooleanField(default=False)
    lift = models.BooleanField(default=False)
    view = models.CharField(max_length=50)

    def __str__(self):
        return self.owner


class Messages(models.Model):
    sender = models.CharField(max_length=200)
    receiver = models.CharField(max_length=200)
    message = models.CharField(max_length=5000)
    valid = models.BooleanField(default=True)
    unread = models.BooleanField(default=True)

    def __str__(self):
        return self.message
