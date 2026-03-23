from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuario

# Listar todos los usuarios
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/lista.html', {'usuarios': usuarios})

# Crear usuario
def crear_usuario(request):
    if request.method == 'POST':
        Usuario.objects.create(
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            email=request.POST['email'],
            telefono=request.POST['telefono'],
        )
        return redirect('lista_usuarios')
    return render(request, 'usuarios/formulario.html', {'accion': 'Crear'})

# Editar usuario
def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.nombre = request.POST['nombre']
        usuario.apellido = request.POST['apellido']
        usuario.email = request.POST['email']
        usuario.telefono = request.POST['telefono']
        usuario.save()
        return redirect('lista_usuarios')
    return render(request, 'usuarios/formulario.html', {'accion': 'Editar', 'usuario': usuario})

# Eliminar usuario
def eliminar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('lista_usuarios')
    return render(request, 'usuarios/confirmar_eliminar.html', {'usuario': usuario})