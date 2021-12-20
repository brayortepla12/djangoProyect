"""shopty URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from webApp.views import homeview,serviciosview,blogview,contactoview,tiendaview
from  django.conf import settings
from  django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homeview.homeView,name='Home'),
    path('servicios/',serviciosview.serviciosView,name='Servicios'),
    path('blog/',blogview.blogView,name='Blog'),
    path('tienda/',tiendaview.tiendaView,name='Tienda'),
    path('contacto/',contactoview.contactoView,name='Contacto'),
]

urlpatterns  += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)