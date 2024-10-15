from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('esignup/',views.eSignupPage,name='esignup'),
    path('elogin/',views.eLoginPage,name='elogin'),
    path('HHome/',views.HomePage,name='HHome'),
    path('logout/',views.LogoutPage,name='logout'),
    path('dashboard/',views.Dashboard,name= 'dashboard'),
    path('wait/',views.wait,name= 'wait'),
    path('expertDashboard/',views.expertDashboard,name= 'expertDashboard'),
    path('knw/',views.knw,name= 'knw'),
    path('chatgpt/',views.chatgpt,name='chatgpt'),
    path('edocs/',views.edocs,name='edocs'),
    path('about/',views.about,name= 'about'),
    path('contact/', views.contact, name= 'contact'),
    path('indexbackend/', views.Indexbackendpage, name= 'indexbackend'),
    path('home/', views.home, name='home'),
    path('<str:room>/', views.room, name='room'),
    path('home/checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    
]
