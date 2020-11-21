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
    pass

def userProfile(request, id):
    user = User.objects.get(id = request.session['userid'])
    # print(user.profilepic)

    context = {
        'user':user,
    }
    return render(request, "userprofile.html", context)


# Create your views here.
