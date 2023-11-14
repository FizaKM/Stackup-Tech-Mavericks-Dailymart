from django.shortcuts import render,redirect
from.models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from Userapp.models import *
# Create your views here.

def adminlogin(request):
    return render(request,'adminlogin.html')

def adminindex(request):
    count1 = Category.objects.all().count()
    count2=Product.objects.all().count()
    count3 = Bookinguser.objects.all().count()
    count4 = Customerregister.objects.all().count()
    count5 = Cart.objects.all().count()
    return render(request,'adminindex.html',{'count1':count1,'count2':count2,'count3':count3,'count4':count4,'count5':count5})

def registeradmin(request):
    return render(request,'registeradmin.html')

def adlogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')    
        request.session['username'] = username
        request.session['password'] = password
        return redirect('adminindex')
    else:
        return render(request,'adminlogin.html')
    
def registerlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username, password=password,email=email)
        if user is not None:
            login(request, user)
            request.session['username_a'] = username
            request.session['email_a'] = email
            request.session['password_a'] = password
            return redirect('registeradmin')
        else:
            return render(request,'registeradmin.html', {'msg':'Sorry Invalid User Credentials'})
    else:
        return render(request, 'registeradmin.html')
    

def addcategory(request):
    return render(request,'addcategory.html')


def viewcategory(request):
    category = Category.objects.all()
    return render(request,'viewcategory.html',{'category':category,})

def getdatacategory(request):
    if request.method=="POST":
        name=request.POST.get('name')
        image=request.FILES.get('image')
        
        data = Category(
            name=name,
            image=image,
        )
        data.save()
        return redirect('viewcategory')
    
def updatecategory(request,id):
    if request.method=="POST":
        name2=request.POST['name']
        try:
            img_c1 = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img_c1.name, img_c1)
        except MultiValueDictKeyError:
            file = Category.objects.get(id=id).image

       
        Category.objects.filter(id=id).update(
            id=id,
            name=name2,
            image=file,
            
          
        )
        return redirect('viewcategory')
    return redirect('viewcategory')

def deletecategory(request,id):
    Category.objects.filter(id=id).delete()

    return redirect('viewbranch')


def editcategory(request, id):
    category = Category.objects.filter(id=id)
    return render(request,'editcategory.html',{'category':category})



def addproduct(request):
    category=Category.objects.all()
    
    return render(request,'addproduct.html',{'category':category})



def viewproduct(request):
    product = Product.objects.all()
   
    return render(request,'viewproduct.html',{'product':product})

def getdataproduct(request):
    if request.method=="POST":
        name=request.POST.get('name')
        category=request.POST.get('category') 
        price=request.POST.get('price')
        image=request.FILES.get('image')
        
        data = Product(
            name=name,
            price=price,
            image=image,
            category=category,
            
        )
        data.save()
        return redirect('viewproduct')



def updateproduct(request,id):
    if request.method=="POST":
        name=request.POST['name']
        category=request.POST.get('category')
       
        price=request.POST.get('price')
        try:
            img_c1 = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img_c1.name, img_c1)
        except MultiValueDictKeyError:
            file = Product.objects.get(id=id).image

       
        Product.objects.filter(id=id).update(
            id=id,
            name=name,
            price=price,
            image=file,
           
            category=category,
            
          
        )
        return redirect('viewproduct')
    return redirect('viewproduct')

def deleteproduct(request,id):
    Product.objects.filter(id=id).delete()

    return redirect('viewproduct')


def editproduct(request, id):
    product = Product.objects.filter(id=id)
    category=Category.objects.all()
    
   
    return render(request,'editproduct.html',{'category':category,'product':product})


def viewcustomerregister(request):
    customerregister = Customerregister.objects.all()
    context = {
        'customerregister':customerregister,
    }

    return render(request,'viewcustomerregister.html',context)




def viewbooking(request):
    bookinguser = Bookinguser.objects.all()
    context = {
        'bookinguser':bookinguser,
    }

    return render(request,'viewbooking.html',context)


def viewmessage(request):
    contactuser =Contactuser.objects.all()
    context = {
        'contactuser':contactuser,
    }
    return render(request,'viewmessage.html',context)

