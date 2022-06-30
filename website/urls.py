from django.contrib import admin
from django.urls import path, include

from .views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('users/', include('users.urls')),
    path('store/', include('store.urls')),
]
