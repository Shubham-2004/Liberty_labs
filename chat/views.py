from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.http import FileResponse
from django.conf import settings
import os

# Create your views here.
def home(request):
    return render(request, 'home.html')
def index(request):
    return render(request, 'index.html')

@login_required(login_url='login')
def HomePage(request):
    return render (request,'HHome.html')
def Indexbackendpage(request):
    return render (request,'indexbackend.html')
def Dashboard(request):
    return render (request,'dashboard.html')
def contact(request):
    return render (request,'contact.html')
def about(request):
    return render (request,'about.html')
def knw(request):
    return render (request,'knw.html')
def chatgpt(request):
    return render (request,'chatgpt.html')
def edocs(request):
    return render (request,'edocs.html')
def wait(request):
    return render (request,'wait.html')
def expertDashboard(request):
    return render (request,'expertDashboard.html')
def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        
    return render (request,'signup.html')
        
def eSignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('elogin')


    return render (request,'esignup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')
def eLoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('wait')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'elogin.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')
def HHome(request):
    return render(request, 'HHome.html')

# def room(request, room):
#     username = request.GET.get('username')
#     room_details = Room.objects.get(name=room)
#     return render(request, 'room.html', {
#         'username': username,
#         'room': room,
#         'room_details': room_details
#     })


def room(request, room):
    try:
        
        username = request.GET.get('username')
        room_details = Room.objects.get(name=room)
        return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })
    except Room.DoesNotExist:
        # Handle the case where the room does not exist, e.g., redirect or show an error message
        return HttpResponse("Room not found", status=404)
    # Continue with the rest of your view logic
    # ...
def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})