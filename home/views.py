from django.shortcuts import render,redirect

from django.contrib.auth.models import User

from django.contrib.auth import authenticate,logout,login

# from django.contrib.auth import logout

# Create your views here.

def index(request):
    if request.user.is_anonymous:
        # print(request.user)
        # print(1)
        return redirect("/login")
    return render(request,"index.html")


def loginUser(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        # print(username,password)

        user = authenticate(username=username, password=password)

        # print(user)

        if user is not None:
            login(request,user)
            return redirect("/")        
        else:
            return render(request,"loginUser.html")

    return render(request,"loginUser.html")


def logoutUser(request):
    logout(request)
    return redirect("/login")