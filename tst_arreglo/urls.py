"""tst_arreglo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from core import views as core_views
from cliente import views as cliente_views


urlpatterns = [
    path('', core_views.home, name='home'),
    path('contact/', core_views.contact, name='contact'),
    path('about/', core_views.about, name='about'),
    path('form_registro/', cliente_views.registro, name='form_registro'),
    path('registrado/',cliente_views.FormularioRegistroView.procesar_formulario, name='registrado'),
    path('servicios/',cliente_views.cliente, name='cliente'),
    path('estatus/',cliente_views.estatus, name='estatus'),
    path('registro_r/',cliente_views.FormularioRegistroView.registro_r, name='registro_r'),
    path('admin/', admin.site.urls),
]
