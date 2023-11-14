from django.urls import path 
from.import views
urlpatterns = [
    path('index/',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('booking/',views.booking,name='booking'),
    path('cart/<int:user_id>/',views.cart,name='cart'),
    path('category/',views.category,name='category'),
    path('product/<str:category>/',views.product,name='product'),
    path('eachproduct/<str:name>/',views.eachproduct,name='eachproduct'),

    path('getdatamessage/',views.getdatamessage,name='getdatamessage'),
    path('getdatabooking/',views.getdatabooking,name='getdatabooking'),
    path('getdatacustomerregister/',views.getdatacustomerregister,name='getdatacustomerregister'),
    

    path('logout1/',views.logout1,name='logout1'),
    path('login1/',views.login1,name='login1'),
    path('register1/',views.register1,name='register1'),
    path('memberlogin/',views.memberlogin,name='memberlogin'),

    path('addtocart/<int:productid>/',views.addtocart,name='addtocart'),
    path('cart/', views.cart, name='cart'),

   
    path('deletecart/<int:id>/',views.deletecart,name='deletecart'),
    path('success/',views.success,name='success'),
    path('success2/',views.success2,name='success2'),

    path('ok/<str:name>/', views.ok, name='ok'),
]