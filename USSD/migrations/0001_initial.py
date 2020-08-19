# Generated by Django 3.0.9 on 2020-08-19 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WhatsAppDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('message', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='WhatsAppRecieved',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PhoneNo', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='WhatsAppSendMSG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('From', models.CharField(max_length=20)),
                ('To', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=5000)),
            ],
        ),
    ]