from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import fooditem,order
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Profile

# Create your views here.
def home(request):
    return render(request,'home.html', {'name' : 'FoodShala'})


#funtion to see food menu
def menu(request):
    obj=fooditem.objects.all()
    return render(request,'menu.html',{'obj': obj})

#function to order food
def orders(request,ab):
    a=request.user
    b=int(a.id)
    c=ab
    o=order.objects.create(cust=b,food=ab)
    o.save()
    return redirect('menu')

#showorder function for restaurents
def showorders(request):
    ob=order.objects.all()
    user=User.objects.all()
    admin=request.user
    restaurent=admin.profile.rest
    rip=fooditem.objects.filter(restaurent=restaurent)
    
    return render(request,'showorders.html',{'ob':ob,'rip':rip,'restaurent':restaurent,'user':user})
                  

#register function
def register(request):
    
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username Taken')
            return redirect('register')
        
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email Already Used')
            return redirect('register')
        
        else:
            user=User.objects.create_user(first_name=first_name,
              last_name=last_name,
              username=username,
              email=email,
              password=password)
            user.save()
            return redirect('login')
        
        
    else:
        return render(request,'register.html')
    
#login function
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        
        if user is None:
            messages.info(request,"You are not Registered!")
            return redirect('login')
        else:
            auth.login(request,user)
            return redirect('/menu')
        
        
    else:  
         return render(request,'login.html')
        
        
#logout function
def logout(request):
    auth.logout(request)
    return redirect('/')
    
