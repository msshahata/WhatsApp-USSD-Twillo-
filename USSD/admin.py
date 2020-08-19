from django.contrib import admin
from .models import WhatsAppDetails,WhatsAppRecieved,WhatsAppSendMSG

# Register your models here.

admin.site.register(WhatsAppDetails)
admin.site.register(WhatsAppRecieved)
admin.site.register(WhatsAppSendMSG)
