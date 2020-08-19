from django.db import models

# Create your models here.


class WhatsAppDetails(models.Model):
    code = models.CharField(max_length = 20, unique=True)
    message = models.TextField(max_length = 5000)

    def __str__(self):
        return self.code


class WhatsAppRecieved(models.Model):
    PhoneNo = models.CharField(max_length = 20)
    message = models.TextField(max_length = 5000)

    def __str__(self):
        return self.PhoneNo

class WhatsAppSendMSG(models.Model):
    From = models.CharField(max_length = 20)
    To = models.CharField(max_length = 20)
    message = models.TextField(max_length = 5000)

    def __str__(self):
        return self.To
