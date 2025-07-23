from django.db import models

class BannerImage(models.Model):
    image = models.ImageField(upload_to="polo_imgs/")

class Chef(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="polo_imgs/")
    about = models.TextField()

class MenuCategory(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="polo_imgs/", blank=True, null=True)

class Menu(models.Model):
    meal = models.CharField(max_length=100)
    ingredient = models.TextField()
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to="polo_imgs/", blank=True, null=True)

class Event(models.Model):
    image = models.ImageField(upload_to="polo_imgs/")
    title = models.CharField(max_length=200)
    content = models.TextField()
    time = models.DateTimeField()

class Reservation(models.Model):
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    people = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    mail = models.EmailField(max_length=256)

class Testimonial(models.Model):
    image = models.ImageField(upload_to="polo_imgs/")
    content = models.TextField()
    name = models.CharField(max_length=70)
    location = models.CharField(max_length=70)
    rait = models.IntegerField(default=0)


