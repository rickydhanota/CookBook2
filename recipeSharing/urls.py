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
    path("createRecipe/", views.createRecipe, name = "createRecipe"),
    path("addRecipe/", views.addRecipe, name = "addRecipe"),
    path("recipeConfirmation/<int:id>/", views.recipeConfirmation, name = "recipeConfirmation"),
    path("dish/delete/<int:id>", views.deleteDish),
    path("dish/edit/<int:id>", views.editDish),
    path("dish/confirmEdits/<int:id>", views.confirmEdits),
    path("popularDesserts/", views.popularDesserts, name = "popularDesserts"),
    path("createDessertRecipe/", views.createDessertRecipe, name = "createDessertRecipe"),
    path("addDessertRecipe/", views.addDessertRecipe, name = "addDessertRecipe"),
    path("dessertConfirmation/<int:id>/", views.dessertConfirmation, name = "dessertConfirmation"),
    path("dessert/delete/<int:id>", views.deleteDish),
    path("dessert/edit/<int:id>", views.editDessert),
    path("dessert/confirmEdits/<int:id>", views.confirmDessertEdits),
    path("addReview/<int:id>/", views.addReview, name = "addReview"),
    path("addDessertReview/<int:id>/", views.addDessertReview, name = "addDessertReview"),

]