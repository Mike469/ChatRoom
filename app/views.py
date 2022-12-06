from django.shortcuts import render, redirect
from app.forms import *
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, admin_only

# Create your views here.

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']

            group = Group.objects.get(name='normal_user')
            user.groups.add(group)

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
        else:
            messages.info(request, 'Username is taken or Passwords do not match.')
            return redirect('register')
    context={'form':form}
    return render(request, 'register.html', context)

def createPage(request):
    form = CreateChannelForm()
    if request.method == 'POST':
        form = CreateChannelForm(request.POST)
        if form.is_valid():
            creation = form.save()
            name = form.cleaned_data['name']
            current_user = request.user

            current_user.add_user.add(Channel.objects.get(name=name))

            context = {'form': form}
            return redirect('view')

    context = {'form': form}
    return render(request, 'create.html', context)

def viewPage(request):
    if request.user.groups.filter(name='admin'):
        channels = Channel.objects.all()
        context = {'channels':channels}
        return render(request, 'view.html', context)
    channels = Channel.objects.filter(user=request.user)
    context = {'channels':channels}
    return render(request, 'view.html', context)

def viewMessages(request, id):
    form = CreateMessageForm()
    if request.method == 'POST':
        form = CreateMessageForm(request.POST)
        if form.is_valid():
            creation = form.save()
            message = form.cleaned_data['message']
            channel = Channel.objects.get(id=id)

            current_message = Message.objects.filter(message=message)
            for current in current_message:
                current.user = request.user
                current.save()     
                channel.add_channel.add(current)

            all_message = Message.objects.filter(channel=Channel.objects.get(id=id))
                        
            return redirect('message', id)
    all_message = Message.objects.filter(channel=Channel.objects.get(id=id))
    context = {'form':form, 'messages':all_message,'id':id}
    return render(request, 'message.html', context)    
    

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin')
        else:
            messages.info(request, "Username OR password is incorrect.")
    context={}
    return render(request, 'login.html', context)

def addUser(request, id):
    all_users = User.objects.all()

    if request.method == 'POST':
        username = request.POST.get('username')

        for user in all_users:
            if str(user) == username:
                user.add_user.add(Channel.objects.get(id=id))
                return redirect('message', id)

    context = {'users':all_users}
    return render(request, 'add.html', context)

def deleteUser(request, id):
    Channel.objects.get(id=id).delete()
    return redirect('view')

def deleteMessage(request, id):
    current = Message.objects.get(id=id)
    current_channel = current.channel.all()[0]
    if request.user == Message.objects.get(id=id).user or request.user.groups.filter(name='admin'):
        current.delete()
        return redirect('message', current_channel.id)
    return redirect('message', current_channel.id)

def updateMessage(request, id):
    current = Message.objects.get(id=id)
    if request.user == Message.objects.get(id=id).user or request.user.groups.filter(name='admin'):
        if request.method == 'POST':
            info = request.POST.get('info')
            current.message = info
            current.save()
            return redirect('message', current.channel.all()[0].id)
        context = {}
        return render(request, 'update.html', context)
    return redirect('message', current.channel.all()[0].id)

def updateChannel(request, id):
    if request.method == 'POST':
        current = Channel.objects.get(id=id)
        info = request.POST.get('info')
        current.name = info
        current.save()
        return redirect('view')
    context={}
    return render(request, 'update.html', context)


@login_required(login_url='login')
@admin_only
def admin_homePage(request):
    context = {}
    return render(request, 'user_home.html', context)

@login_required(login_url='login')
def userPage(request):
    context = {}
    return render(request, 'user_home.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')



