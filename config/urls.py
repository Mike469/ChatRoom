"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', registerPage, name='register'),
    path('login/', loginPage, name='login'),
    path('admin-home/', admin_homePage, name='admin'),
    path('logout/', logoutUser, name='logout'),
    path('user-home/', userPage, name='user-page'),
    path('user-home/create/', createPage, name='create'),
    path('user-home/view/', viewPage, name='view'),
    path('user-home/message/<int:id>/', viewMessages, name='message'),
    path('user-home/add-user/<int:id>/', addUser, name='add'),
    path('user/channel/delete/<int:id>', deleteUser, name='delete_channel'),
    path('user/channel/update/<int:id>', updateChannel, name='update_chan'),
    path('user/message/delete/<int:id>', deleteMessage, name='delete_message'),
    path('user/message/update/<int:id>', updateMessage, name='update_msg')
]
