
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('diario_reumatico/',include('diario_reumatico.urls')),
]
