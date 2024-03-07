from django.http import HttpResponse

from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from.models import Admin,Register,Packages
def ttmhome(request):
    return render(request, "ttmhome.html")

def loginfail(request):
    return render(request, "loginfail.html")

def checkadminlogin(request):
    if request.method == "POST":
        name = request.POST["uname"]
        pwdd = request.POST["pwd"]
        flag=Register.objects.filter(username=name,password=pwdd).values()
        if flag: #flag is not null or not empty
            if name=="amrutha":
                messages.info(request,"This is admin's TTM page")
                return render(request,"adminhome.html")
        if flag:
            messages.info(request, "This is user's TTM page")
            return render(request, "ttmhome.html")
        else:
            messages.info(request,"Invalid Credentials!!")
            return render(request, "loginfail.html")
def checkregistration(request):
    if request.method  == "POST":
         name = request.POST["name"]
         addr = request.POST["addr"]
         email = request.POST["email"]
         phno = request.POST["phno"]
         uname = request.POST["uname"]
         pwd = request.POST["pwd"]
         cpwd = request.POST["cpwd"]
         if pwd==cpwd:
             if Register.objects.filter(username=uname).exists():
                 messages.info(request,"username existing..!!")
                 return render(request,"register.html")
             elif Register.objects.filter(email=email).exists():
                 messages.info(request,"email existing..!!")
                 return render(request,"register.html")
             else:
                 user=Register.objects.create(name=name,address=addr,email=email,phno=phno,username=uname,password=pwd)
                 user.save()
                 messages.info(request,"user created")
                 return render(request,"login.html")
         else:
             messages.info(request,"password not matching..!!")
             return render(request,"register.html")
def checkpackages(request):
    if request.method == "POST":
        tcode = request.POST["tourcode"]
        tname = request.POST["tourname"]
        tpack = request.POST["tourpackage"]
        tdesc = request.POST["desc"]
        pack= Packages.objects.create(tourcode=tcode,tourname=tname,tourpackage=tpack,desc=tdesc)
        pack.save()
        messages.info(request,"Data Inserted Sucessfully🥳")
        return render(request,"package.html")
    else:
        return render(request, "package.html")
def viewplaces(request):
    data = Packages.objects.all()
    return render(request,"viewplaces.html",{"placesdata":data})
def checkChangePassword(request):
    if request.method=="POST":
        uname=request.POST["uname"]
        opwd=request.POST["opwd"]
        npwd=request.POST["npwd"]
        flag=Register.objects.filter(username=uname,password=opwd).values()
        if flag:
            Register.objects.filter(username=uname,password=opwd).update(password=npwd)
            messages.info(request, "Password Updated")
            return render(request,"index.html")
        else:
            return render(request,"index.html")
    else:
        return render(request,"changepassword.html")
def logout(request):
    messages.info(request,"logout")
    return render(request,"index.html")
