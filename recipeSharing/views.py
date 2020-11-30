from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
import bcrypt

def index(request):
    if 'userid' in request.session:
        user = User.objects.get(id = request.session['userid'])
        context = {
            'user':user,
        }
        return render(request, 'index.html',context)
    else:
        return render(request,'index.html')

def sign_in(request):
    return render(request, "sign_in.html")

def register_form(request):
    return render(request, "register_form.html")

def registration(request):
    errors = User.objects.basic_validator(request.POST, 'registration')
    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request,value)
        return redirect('/register_form')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        
        logged_user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = pw_hash)
        #Removed the phone info for the logged_user
        request.session['userid'] = logged_user.id

        return redirect('/')

def login(request):
    errors = User.objects.basic_validator(request.POST, 'login')
    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request,value)
        return redirect('/sign_in')
    else:
        user = User.objects.filter(email=request.POST['email'])
        if user:
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['userid'] = logged_user.id
                return redirect("/") #redirect to success route
        # return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')

def founders(request):
    user = User.objects.get(id = request.session['userid'])
    context = {
        'user':user,
    }
    return render(request, "founders.html", context)

def popularDishes(request):
    user = User.objects.get(id = request.session['userid'])
    dishes = Recipe.objects.all()
    # print(user.profilepic)

    context = {
        'user':user,
        "dishes": dishes,
    }
    return render(request, "popularDishes.html", context) 

def userProfile(request, id):
    user = User.objects.get(id = request.session['userid'])
    # print(user.profilepic)

    context = {
        'user':user,
    }
    return render(request, "userprofile.html", context)

def createRecipe(request):
    if 'userid' not in request.session:
        return redirect('/')

    user = User.objects.get(id=request.session['userid'])
    context = {
        "user": user
    }

    return render(request, 'createRecipe.html', context)

def addRecipe(request):
    if 'userid' not in request.session:
        return redirect('/')

    # if request.method == "POST":
    #     # request.Files used for uploading anything
    #     pic = request.FILES["Image"]
    # fs = FileSystemStorage()
    # user_pic = fs.save(pic.name, pic)
    # url = fs.url(user_pic)
    user = User.objects.get(id=request.session['userid'])

    dish = Recipe.objects.create(title = request.POST["recipeName"], description = request.POST["description"], ingredients = request.POST["ingredients"], steps = request.POST["steps"], dishImage = request.FILES["Image"], user = user)

    return redirect(f'/recipeConfirmation/{dish.id}/')

def recipeConfirmation(request, id):
    dish = Recipe.objects.get(id = id)
    user = User.objects.get(id=request.session['userid'])

    context = {
        "user": user,
        "dish": dish,
    }
    return render(request, "recipeConfirmation.html", context)

def deleteDish(request, id):
    user = User.objects.get(id=request.session['userid'])
    dish = Recipe.objects.get(id = id)
    dish.delete()
    return redirect("/popularDishes/")

def editDish(request, id):
    dish = Recipe.objects.get(id = id)
    user = User.objects.get(id=request.session['userid'])

    context = {
        "user": user,
        "dish": dish,
    }
    return render(request, "editDish.html", context)


def confirmEdits(request, id):
    user = User.objects.get(id=request.session['userid'])
    dish = Recipe.objects.get(id = id)
    dish.title = request.POST["recipeName"]
    dish.description = request.POST["description"]
    dish.ingredients = request.POST["ingredients"]
    dish.steps = request.POST["steps"]
    dish.save()
    return redirect(f"/recipeConfirmation/{dish.id}/")

def popularDesserts(request):
    user = User.objects.get(id = request.session['userid'])
    desserts = Dessert.objects.all()
    # print(user.profilepic)

    context = {
        'user':user,
        "desserts": desserts,
    }
    return render(request, "popularDesserts.html", context)

def createDessertRecipe(request):
    if 'userid' not in request.session:
        return redirect('/')

    user = User.objects.get(id=request.session['userid'])
    context = {
        "user": user
    }

    return render(request, 'createDessertRecipe.html', context)

def addDessertRecipe(request):
    if 'userid' not in request.session:
        return redirect('/')

    # if request.method == "POST":
    #     # request.Files used for uploading anything
    #     pic = request.FILES["Image"]
    # fs = FileSystemStorage()
    # user_pic = fs.save(pic.name, pic)
    # url = fs.url(user_pic)
    user = User.objects.get(id=request.session['userid'])

    dessert = Dessert.objects.create(title = request.POST["recipeName"], description = request.POST["description"], ingredients = request.POST["ingredients"], steps = request.POST["steps"], dessertImage = request.FILES["Image"], user = user)

    return redirect(f'/dessertConfirmation/{dessert.id}/')

def dessertConfirmation(request, id):
    dessert = Dessert.objects.get(id = id)
    user = User.objects.get(id=request.session['userid'])

    context = {
        "user": user,
        "dessert": dessert,
    }
    return render(request, "dessertConfirmation.html", context)

def deleteDessert(request, id):
    user = User.objects.get(id=request.session['userid'])
    dessert = Dessert.objects.get(id = id)
    dessert.delete()
    return redirect("/popularDesserts/")

def editDessert(request, id):
    dessert = Dessert.objects.get(id = id)
    user = User.objects.get(id=request.session['userid'])

    context = {
        "user": user,
        "dessert": dessert,
    }
    return render(request, "editDessert.html", context)


def confirmDessertEdits(request, id):
    user = User.objects.get(id=request.session['userid'])
    dessert = Dessert.objects.get(id = id)
    dessert.title = request.POST["recipeName"]
    dessert.description = request.POST["description"]
    dessert.ingredients = request.POST["ingredients"]
    dessert.steps = request.POST["steps"]
    dessert.save()
    return redirect(f"/dessertConfirmation/{dessert.id}/")

def addReview(request, id):
    user = User.objects.get(id=request.session['userid'])
    dish = Recipe.objects.get(id = id)
    this_review = Review.objects.create(feedback = request.POST["review"], rating = request.POST["rate"], recipe = dish, users = user)

    context = {
        "user": user,
        "this_review": this_review,
        "dish": dish,
    }

    return render(request, "reviewPartial.html", context)


def addDessertReview(request, id):
    user = User.objects.get(id=request.session['userid'])
    dessert = Dessert.objects.get(id = id)
    this_dessert = DessertReview.objects.create(feedback = request.POST["review"], rating = request.POST["rate"], dessert = dessert, users = user)

    context = {
        "user": user,
        "this_dessert": this_dessert,
        "dessert": dessert,
    }
    print("made it to the end of python")

    return render(request, "reviewDessertPartial.html", context)


# Create your views here.