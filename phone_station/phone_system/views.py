from django.shortcuts import render
from .models import Client, Phone, Conversation, Tariff

def project_info(request):
    clients = Client.objects.all()
    phones = Phone.objects.all()
    conversations = Conversation.objects.all()
    tariffs = Tariff.objects.all()

    return render(request, 'project_info.html', {
        'clients': clients,
        'phones': phones,
        'conversations': conversations,
        'tariffs': tariffs,
    })