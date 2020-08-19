"""WhatsApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from USSD import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.SignIn_page, name = 'SignIn'),
    url(r'^RMSG/',views.ReceivedMSG, name = 'ReceivedMSG'),
    url(r'^SMSG/',views.SendMsg, name = 'SendMsg'),
    url(r'^ADD/',views.AddCode, name = 'ADD'),
    url(r'^HOME/',views.Home, name = 'Home'),
    url(r'^logout/',views.logout_user, name = 'logout'),
    url(r'^MList/',views.MessageList, name = 'MessageList'),
    url(r'^RMList/',views.RMessageList, name = 'RMessageList'),
    url(r'^SMList/',views.SMessageList, name = 'SMessageList'),

    
]
