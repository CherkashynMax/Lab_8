from django.contrib import admin
from django.urls import path, include
import phone_system.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(phone_system.urls)),

]