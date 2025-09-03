from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Producto
from .forms import ProductoForm
from django.contrib.auth import logout
from django.shortcuts import redirect

@login_required
def producto_list(request):
    q = request.GET.get('q','').strip()
    productos = Producto.objects.all().order_by('id') #agregue el orden del id
    if q:
        productos = productos.filter(nombre__icontains=q)
    return render(request, 'producto_list.html', {'productos': productos, 'q': q})

@login_required
def producto_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto creado.')
            return redirect('producto_list')
    else:
        form = ProductoForm()
    return render(request, 'producto_form.html', {'form': form, 'titulo':'Nuevo producto'})

@login_required
def producto_update(request, pk):
    obj = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado.')
            return redirect('producto_list')
    else:
        form = ProductoForm(instance=obj)
    return render(request, 'producto_form.html', {'form': form, 'titulo':'Editar producto'})

@login_required
def producto_delete(request, pk):
    obj = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Producto eliminado.')
        return redirect('producto_list')
    return render(request, 'producto_confirm_delete.html', {'obj': obj})

def logout_view(request):
    logout(request)
    return redirect('login')  # o a donde quieras redirigir