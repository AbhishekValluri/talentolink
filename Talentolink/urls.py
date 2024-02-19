"""
URL configuration for Talentolink project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from jobportal import views # importing the urls from the app jobportal in that views.py

# importing the settings and media urls to integrate
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # name= is used url routing in the navigation bar
    path('', views.Home,name='Home'), # client requesting urls
    path('about/',views.About,name='About'),
    path('service/', views.Service,name='Service'),
    path('contact/', views.Contact,name='Contact'),
    path('employee/', views.Employee,name='Employee'),
    path('Login/', views.Login,name='Login'),
    path('register/', views.Register,name='Register'),
    path('job/', views.Job,name='Job'),
    path('result/', views.Result,name='Result')
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
