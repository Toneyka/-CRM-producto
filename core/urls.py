from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from inventario import views as inv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'), #agregue recien 
    
    # Auth
    path('login/',  auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    # Productos
    
    path('', inv.producto_list, name='producto_list'),
    path('productos/nuevo/', inv.producto_create, name='producto_create'),
    path('productos/<int:pk>/editar/', inv.producto_update, name='producto_update'),
    path('productos/<int:pk>/eliminar/', inv.producto_delete, name='producto_delete'),
]
