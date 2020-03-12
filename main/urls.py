from django.urls import path
from . import views
# 
urlpatterns =[
    path('',views.home, name='home'),path('menu',views.menu,name='menu'),path('register',views.register, name='register'),path('login',views.login,name='login'),path('logout',views.logout, name='logout'),path('orders/<ab>/',views.orders, name='orders'),path('showorders',views.showorders, name='showorders')
]