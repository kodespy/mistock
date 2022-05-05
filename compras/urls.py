from django.urls import path 

from django.contrib.auth import views as auth_views

from .views import ProveedorView, ProveedorNew, ProveedorEdit, ProveedorVer, \
 proveedorEstado, ComprarView




urlpatterns = [
    path('proveedores/', ProveedorView.as_view(), name='proveedor_list'),
    path('proveedores/ver/<int:pk>', ProveedorVer.as_view(), name='proveedor_ver'),    
    path('proveedores/new', ProveedorNew.as_view(), name='proveedor_new'),
    path('proveedores/edit/<int:pk>', ProveedorEdit.as_view(), name='proveedor_edit'),    
    path('proveedores/estado/<int:pk>/<estado>', proveedorEstado, name='proveedorEstado'),    
    path('comprar/', ComprarView.as_view(), name='comprar_list'),

 
]
