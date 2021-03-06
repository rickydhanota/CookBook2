from __future__ import unicode_literals
from django.db import models
import re, bcrypt
from django.core.validators import MaxValueValidator, MinValueValidator


class UserManager(models.Manager):
    def basic_validator(self, postData, sign_in):
        errors = {}
        if sign_in == 'registration':
            if len(postData['first_name'])<2:
                errors['first_name'] = "First name needs to be longer than 2 characters"
            if len(postData['last_name'])<2:
                errors['last_name'] = "Last name needs to be longer than 2 characters"
            if len(postData['password'])<8:
                errors['password'] = "Password needs to be longer than 8 characters"
            if postData['confirm_password'] != postData['password']:
                errors['confirm_password'] = "Passwords do NOT match"

            EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
            if not EMAIL_REGEX.match(postData['email']): # test whether a field matches the pattern
                errors['email'] = ("Invalid email address!")

        elif sign_in == 'login':
            user = User.objects.filter(email=postData['email'])
            if not user:
                errors['user_login'] = 'Incorrect email'
            else:
                if not bcrypt.checkpw(postData['password'].encode(), user[0].password.encode()):
                    errors['user_password'] = 'Incorrect Password'

        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

class Recipe(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    ingredients = models.TextField()
    steps = models.TextField()
    dishImage = models.ImageField(upload_to='images/', null = True)
    user = models.ForeignKey(User, related_name = "recipes", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

class Dessert(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    ingredients = models.TextField()
    steps = models.TextField()
    dessertImage = models.ImageField(upload_to='images/', null = True)
    user = models.ForeignKey(User, related_name = "dessert_recipes", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

class Review(models.Model):
    feedback = models.TextField()
    rating = models.IntegerField(default = 0,
        validators = [
                MaxValueValidator(5),
                MinValueValidator(0),
            ]
        )
    users = models.ForeignKey(User, related_name = "reviews", on_delete = models.CASCADE)
    recipe = models.ForeignKey(Recipe, related_name = "reviews", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

class DessertReview(models.Model):
    feedback = models.TextField()
    rating = models.IntegerField(default = 0,
        validators = [
                MaxValueValidator(5),
                MinValueValidator(0),
            ]
        )
    users = models.ForeignKey(User, related_name = "dessert_reviews", on_delete = models.CASCADE)
    dessert = models.ForeignKey(Dessert, related_name = "reviews", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)


# Create your models here.
