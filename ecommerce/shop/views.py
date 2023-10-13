from django.shortcuts import render
from shop.models import Category,Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def allprodcat(request):
    c=Category.objects.all()
    return render(request,'category.html',{'c':c})

def allproducts(request,c):
    p=Product.objects.filter(category__cname=c)
    category=Category.objects.get(cname=c)
    return render(request,'products.html',{'p':p,'category':category})

def productdetails(request,p):
    d=Product.objects.get(pname=p)
    return render(request,'productdetails.html',{'d':d})

def user_signup(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p1=request.POST['p1']
        p2=request.POST['p2']
        f=request.POST['f']
        l=request.POST['l']
        e=request.POST['e']
        if(p1==p2):
            u=User.objects.create_user(username=u,password=p1,first_name=f,last_name=l,email=e)
            u.save()
            return allprodcat(request)
    return render(request,'signup.html')


def user_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p1=request.POST['p1']
        user=authenticate(username=u,password=p1)
        if user:
            login(request,user)
            return allprodcat(request)
        else:
            messages.error(request,'Invalid Credentials')
    return render(request,'login.html')


def user_logout(request):
    logout(request)
    return user_login(request)

