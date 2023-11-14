from django.shortcuts import render,redirect
from.models import *
from django.db.models import F, Sum, FloatField
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.

def index(request):
    user_id = request.session.get('uid')
    category=Category.objects.all()
    num=Cart.objects.filter(user_id=user_id,status=0).count()
    return render(request,'index.html',{'category':category,'num':num})


def about(request):
    user_id = request.session.get('uid')
    num=Cart.objects.filter(user_id=user_id,status=0).count()
    return render(request,'about.html',{'num':num})



def contact(request):
    user_id = request.session.get('uid')
    num=Cart.objects.filter(user_id=user_id,status=0).count()
    return render(request,'contact.html',{'num':num})

def product(request,category):
    user_id = request.session.get('uid')
    num=Cart.objects.filter(user_id=user_id,status=0).count()
    product=Product.objects.filter(category=category)
    return render(request,'product.html',{'product':product,'num':num})

def eachproduct(request,name):
    user_id = request.session.get('uid')
    num=Cart.objects.filter(user_id=user_id,status=0).count()
    product=Product.objects.filter(name=name)
    
    return render(request,'eachproduct.html',{'product':product,'num':num})

def category(request):
    user_id = request.session.get('uid')
    category=Category.objects.all()
    num=Cart.objects.filter(user_id=user_id,status=0).count()
    return render(request,'category.html',{'category':category,'num':num})


def booking(request):
    user_id = request.session.get('uid')
    data = Cart.objects.filter(user_id=user_id,status=0)
    total = Cart.objects.filter(user_id=user_id,status=0).aggregate(Sum('total'))
    num=Cart.objects.filter(user_id=user_id,status=0).count()
    return render(request,'booking.html',{'data':data,'total':total,'num':num})

def getdatamessage(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        
        
        data = Contactuser(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )
        data.save()
        return redirect('success2')
    
def getdatacustomerregister(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        
        data = Customerregister(
            name=name,
            email=email,
           password=password,
        )
        data.save()
        return redirect('index')
    

def getdatabooking(request):
    
    if request.method=="POST":
        user_id = request.session.get('uid')
        name=request.POST.get('name')
        phonenumber=request.POST.get('phonenumber')
        
        address=request.POST.get('address')
        zipcode=request.POST.get('zipcode')
        booked=Cart.objects.filter(user_id=user_id,status=0)
        for i in booked:

        
        
            data =Bookinguser(
                cartid=Cart.objects.get(id=i.id),user_id=Customerregister.objects.get(id=user_id),name=name,phonenumber=phonenumber,
            
            address=address,
            zipcode=zipcode,
            )
            data.save()
            Cart.objects.filter(id=i.id).update(status=1)
        return redirect('success')



def success(request):
    user_id = request.session.get('uid')
    num=Cart.objects.filter(user_id=user_id,status=0).count()
    return render(request,'success.html',{'num':num})

def success2(request):
    user_id = request.session.get('uid')
    num=Cart.objects.filter(user_id=user_id,status=0).count()
    return render(request,'success2.html',{'num':num})

def login1(request):
    return render(request,'login1.html')

def register1(request):
    return render(request,'register1.html')
       
def memberlogin(request):
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        if Customerregister.objects.filter(name=name,password=password).exists():
            data = Customerregister.objects.filter(name=name,password=password).values('email','id').first()
            
            request.session['email'] = data['email']
            
            request.session['name'] = name
            request.session['password'] = password
            request.session['uid'] = data['id']
            return redirect('index')
        else:
            return render(request,'login1.html',{'msg':"Invalid Login Id.Please Register"})
    else:
        return render(request,'login1.html')
    
def addtocart(request,productid):
    if request.method == "POST":
        user_id = request.session.get('uid') 
        quantity=request.POST.get('quantity')
        product=Product.objects.get(id=productid)
        
        try:
            total = request.POST['total']
        except MultiValueDictKeyError:
            total = False
        data = Cart(user_id=Customerregister.objects.get(id=user_id), productid=product,quantity=quantity, total=total, status=0)
        print(data)
        data.save()
        return redirect('cart')
    
    

def cart(request):
    
    user_id = request.session.get('uid')
    print(user_id)
    if user_id is not None:
        data = Cart.objects.filter(user_id=user_id,status=0)
        total = Cart.objects.filter(user_id=user_id,status=0).aggregate(Sum('total'))
        
        num=Cart.objects.filter(user_id=user_id,status=0).count()

        return render(request,'cart.html',{'data':data,'total':total,'cart':cart,'num':num,})
    else:
         return render(request,'cart.html')

def deletecart(request,id):
    Cart.objects.filter(id=id).delete()
    return redirect('cart')




def logout1(request):
    del request.session['email']
    del request.session['name']
    del request.session['password']    
    del request.session['uid']
    return redirect('index')


def ok(request,name):
    product = Product.objects.filter(name=name)
    context = {'product': product}
    return render(request, 'eachproduct.html', context)