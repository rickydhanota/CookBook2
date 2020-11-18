from django.shortcuts import render, redirect, HttpResponse

def index(request):
    if 'userid' in request.session:
        user = User.objects.get(id = request.session['userid'])
        context = {
            'user':user,
        }
        return render(request, 'index.html',context)
    else:
        return render(request,'index.html')


# Create your views here.
