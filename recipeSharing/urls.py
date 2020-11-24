from django.urls import path 
from . import views

urlpatterns = [
    path("", views.index, name = "home"),
    path("sign_in/", views.sign_in, name = "sign_in"),
    path("register_form/", views.register_form, name = "register_form"),
    path("registration/", views.registration, name = "registration"),
    path("login/", views.login, name = "login"),
    path("logout/", views.logout, name = "logout"),
    path("founders/", views.founders, name = "founders"),
    path("popularDishes/", views.popularDishes, name = "popularDishes"),
    path('userprofile/<int:id>/', views.userProfile),
    path("createRecipe", views.createRecipe, name = "createRecipe"),
    path("addRecipe", views.addRecipe, name = "addRecipe"),
    path("recipeConfirmation/<int:id>/", views.recipeConfirmation, name = "recipeConfirmation"),
]