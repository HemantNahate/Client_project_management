"""
URL configuration for client_project_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# client_project_system/urls.py
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Simple view to show a message on the root URL
def home(request):
    return HttpResponse("Welcome to the Client-Project System API!")

urlpatterns = [
    path('', home),  # This will make the root URL display a message
    path('admin/', admin.site.urls),
    path('api/', include('clients.urls')),  # Include API routes from the clients app
]
