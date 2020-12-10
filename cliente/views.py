from django.shortcuts import render, HttpResponse
from .forms import FormularioCliente
from .models import Registro
# Create your views here.
class FormularioRegistroView(HttpResponse):
    def registro_r(request):
        cliente_r = FormularioCliente()
        return render(request, 'cliente/registro.html',{'form':cliente_r})

    def procesar_formulario(request):
        cliente_r = FormularioCliente(request.POST)
        if cliente_r.is_valid():
            cliente_r.save()
            cliente_r = FormularioCliente()
        return render(request, 'cliente/registro.html',{'form':cliente_r, 'mensaje':'ok'})

    def obtener_id(request,registro_id):
        registro=get_object_or_404(FormularioCliente,id=registro_id)
        posts=Post.objects.filter(categories=registro)
        return render(request,"cliente/registrado.html",{"category":category,"posts":posts})    

def cliente(request):
    return render(request, 'cliente/cliente.html')

def registro(request):
    return render(request, 'cliente/form_registro.html')

def registrado(request):
    return render(request, 'cliente/registrado.html')

def estatus(request):
    return render(request, 'cliente/estatus_reparacion.html')

