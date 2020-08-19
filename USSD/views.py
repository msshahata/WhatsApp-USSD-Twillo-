from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from twilio.twiml.messaging_response import MessagingResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from requests.auth import HTTPBasicAuth
import requests
from django.urls import reverse
from twilio.rest import Client
from .models import WhatsAppDetails,WhatsAppRecieved,WhatsAppSendMSG
from .forms import WhatsAppDetailsForm,WhatsAppSendMSGForm
import os
import psycopg2
from django.core.exceptions import ObjectDoesNotExist
DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')


def SignIn_page(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username , password= password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('Home'))
            else:
                messages.info(request,'The User is Not Active')
                return HttpResponseRedirect(reverse('SignIn'))

        else:
            messages.info(request,'The Username or Password is Incorrect')
            return HttpResponseRedirect(reverse('SignIn'))


    else:
        return render(request,'login.html',{})

@login_required(login_url = 'SignIn')
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('SignIn'))


@csrf_exempt
def ReceivedMSG(request):
        try:
            resp = MessagingResponse()
            body = request.POST.get('Body', None)
            PhoneNo = request.POST.get('From', None)
            details = WhatsAppDetails.objects.get(code = body)
            result = details.message
            resp.message(result)
            savedataRec = WhatsAppRecieved(message =body,PhoneNo=PhoneNo)
            savedataRec.save()
            return HttpResponse(resp)
        except WhatsAppDetails.DoesNotExist:
            result = 'مرحبا بكم في الخدمة التجريبية لديوان الزكاة، لبدء الخدمة قم بإعادة إرسال كلمة بدء'
            resp.message(result)
            return HttpResponse(resp)


@login_required(login_url = 'SignIn')
@csrf_exempt
def SendMsg(request):
    if request.method =='POST':
        account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
        auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
        client = Client(account_sid, auth_token)
        getform = WhatsAppSendMSGForm(data=request.POST)
        if getform.is_valid():
            From = getform.cleaned_data['From']
            To = getform.cleaned_data['To']
            Message = getform.cleaned_data['message']
            savedata = WhatsAppSendMSG(From =From, To=To,message=Message)
            savedata.save()
            message = client.messages.create(
                                      body= Message,
                                      from_='whatsapp:'+ From ,
                                      to='whatsapp:'+ To
                                  )
            getform = WhatsAppSendMSGForm()
            return render(request,'SendMsg.html',{'DForms':getform})

        else:
            getform = WhatsAppSendMSGForm()
            return render(request,'SendMsg.html',{'DForms':getform})
    else:
        getform = WhatsAppSendMSGForm()
        return render(request,'SendMsg.html',{'DForms':getform})


@login_required(login_url = 'SignIn')
def AddCode(request):
    if request.method =='POST':
        getform = WhatsAppDetailsForm(data=request.POST)
        if getform.is_valid():
            Code = getform.cleaned_data['code']
            Message = getform.cleaned_data['message']
            savedata = WhatsAppDetails(code =Code,message=Message)
            savedata.save()
            getform = WhatsAppDetailsForm()
            return HttpResponseRedirect(reverse('MessageList'))
        else:
            messages.error(request, 'This Code has been use')
            getform = WhatsAppDetailsForm()
            return render(request,'AddCode.html',{'Forms':getform})
    else:
        getform = WhatsAppDetailsForm()
        return render(request,'AddCode.html',{'Forms':getform})

@login_required(login_url = 'SignIn')
def Home(request):
    return render(request,'Home.html')

@login_required(login_url = 'Sigin')
def MessageList(request):
    Messages_Show = WhatsAppDetails.objects.all()
    return render(request,'MessageList.html',{'Messages_Show':Messages_Show})

@login_required(login_url = 'Sigin')
def RMessageList(request):
    Messages_Show = WhatsAppRecieved.objects.all()
    return render(request,'RMesList.html',{'Messages_Show':Messages_Show})

@login_required(login_url = 'Sigin')
def SMessageList(request):
    Messages_Show = WhatsAppSendMSG.objects.all()
    return render(request,'SMesList.html',{'Messages_Show':Messages_Show})
