from django.contrib import admin
from .models import Client, Phone, Conversation, Tariff


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_code', 'client_type', 'address', 'last_name', 'first_name', 'middle_name')

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'client_code')

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('conversation_code', 'conversation_date', 'phone_number', 'conversation_minutes', 'tariff_code')

@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    list_display = ('tariff_code', 'call_type', 'cost_per_minute')

