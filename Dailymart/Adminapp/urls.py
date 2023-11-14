from django.urls import path 
from.import views

urlpatterns = [
    path('',views.adminlogin,name='adminlogin'),
    path('adlogin/',views.adlogin,name='adlogin'),
    path('registerlogin/',views.registerlogin,name='registerlogin'),
    path('adminindex/',views.adminindex,name='adminindex'),
    path('registeradmin/',views.registeradmin,name='registeradmin'),

    path('addproduct/',views.addproduct,name='addproduct'),
    path('viewproduct/',views.viewproduct,name='viewproduct'),
    path('getdataproduct/',views.getdataproduct,name='getdataproduct'),
    path('editproduct/<int:id>/',views.editproduct,name='editproduct'),
    path('updateproduct/<int:id>', views.updateproduct, name='updateproduct'),
    path('deleteproduct/<int:id>/',views.deleteproduct,name='deleteproduct'),

    

    path('addcategory/',views.addcategory,name='addcategory'),
    path('viewcategory/',views.viewcategory,name='viewcategory'),
    path('getdatacategory/',views.getdatacategory,name='getdatacategory'),
    path('editcategory/<int:id>/',views.editcategory,name='editcategory'),
    path('updatecategory/<int:id>', views.updatecategory, name='updatecategory'),
    path('deletecategory/<int:id>/',views.deletecategory,name='deletecategory'),


   
    path('viewcustomerregister/',views.viewcustomerregister,name='viewcustomerregister'),

    path('viewbooking/',views.viewbooking,name='viewbooking'),
 
    path('viewmessage/',views.viewmessage,name='viewmessage'),
   


]
