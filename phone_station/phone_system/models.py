from django.db import models

class Client(models.Model):
    client_code = models.AutoField(primary_key=True)
    client_type = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)

class Phone(models.Model):
    phone_number = models.CharField(max_length=15, primary_key=True)
    client_code = models.ForeignKey(Client, on_delete=models.CASCADE)

class Conversation(models.Model):
    conversation_code = models.AutoField(primary_key=True)
    conversation_date = models.DateField()
    phone_number = models.CharField(max_length=15)
    conversation_minutes = models.IntegerField()
    tariff_code = models.ForeignKey('Tariff', on_delete=models.CASCADE)

class Tariff(models.Model):
    tariff_code = models.AutoField(primary_key=True)
    call_type = models.CharField(max_length=50)
    cost_per_minute = models.DecimalField(max_digits=5, decimal_places=2)