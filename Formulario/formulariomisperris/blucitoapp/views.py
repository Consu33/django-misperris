<<<<<<< HEAD
from django.http import HttpResponse


def hola_mundo(request):
    return HttpResponse("Hola mundo")

=======
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
>>>>>>> 6980591633ff7f4dad85c9794d0d64c171502f16

