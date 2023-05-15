from django.shortcuts import render
from django.http import HttpResponseRedirect
from blucitoapp.models import Usuario



def formulario(request):
    return render(request, 'formulario.html')

def formulario(request):
    if request.method == 'POST':
        correo = request.POST['correo']
        apellido = request.POST['apellido']
        nombre = request.POST['nombre']
        telefono = request.POST['telefono']
        direccion = request.POST['direccion']
        comuna = request.POST['comuna']
        usuario = Usuario(correo=correo, apellido=apellido, nombre=nombre, telefono=telefono, direccion=direccion, comuna=comuna)
        usuario.save()
        return HttpResponseRedirect('/formulario/')
    else:
        return render(request, 'formulario.html')

