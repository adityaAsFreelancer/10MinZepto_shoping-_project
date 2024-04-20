from django.urls import path
from . import views
urlpatterns=[
    path('',views.home),
    path('home/',views.home),
    path('about/',views.about),
    path('contact/',views.contact),
    path('signup/',views.signup),
    path('signin/',views.signin),
    path('product/',views.product),
    path('signout/',views.signout),
    path('myprofile/',views.myprofile),
    path('mycart/',views.mycart),
    path('indexcart/',views.indexcart),
    path('cartitems/',views.cartitems),
    path('myorders/',views.myorders),
    path('orderitem/',views.orderitems),
]