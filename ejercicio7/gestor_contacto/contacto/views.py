from django.shortcuts import render, redirect, get_object_or_404
from .models import Contacto
from .forms import FormularioContacto

#1. Mostrar todos los contactos
def contacto_lista (request):
    contacto = Contacto.objects.all()
    return render(request, 'contacto/contacto_lista.html', {'contacto': contacto})


#2. agregar contatco

def contacto_agregar(request):
    if request.method == 'POST':
        formulario = FormularioContacto(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('contacto_lista')
    else:
        formulario = FormularioContacto()

    return render(request, 'contacto/contacto_formulario.html',{'formulario':formulario})

#crud : 

def contacto_actualizar(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    if request.method == 'POST':
        formulario = FormularioContacto(request.POST, instance=contacto)
        if formulario.is_valid():
            formulario.save()
            return redirect ('contacto_lista')
    else:
        formulario=FormularioContacto(instance=contacto)

    return render(request, 'contacto/contacto_formulario.html', {'formulario':formulario})

def contacto_eliminar(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)  
    if request.method == 'POST':
        contacto.delete()
        return redirect('contacto_lista')  
    return render(request,'contacto/contacto_confirmar_eliminar.html', {'contacto':contacto})