from django.urls import path 

from django.contrib.auth import views as auth_views

from .views import MonedaView, MonedaNew, MonedaEdit, MonedaVer, monedaEstado, \
    MarcaView, MarcaNew, MarcaEdit, MarcaVer, marcaEstado, \
    CategoriaView, CategoriaNew, CategoriaEdit, CategoriaVer, categoriaEstado, \
    SubCategoriaView, SubCategoriaNew, SubCategoriaEdit, SubCategoriaVer, subcategoriaEstado, \
    ProductoView, ProductoNew, ProductoEdit, ProductoVer, productoEstado

urlpatterns = [
    path('monedas/', MonedaView.as_view(), name='moneda_list'),
    path('monedas/ver/<int:pk>', MonedaVer.as_view(), name='moneda_ver'),
    path('monedas/new', MonedaNew.as_view(), name='moneda_new'),
    path('monedas/edit/<int:pk>', MonedaEdit.as_view(), name='moneda_edit'),    
    path('monedas/estado/<int:pk>/<estado>', monedaEstado, name='monedaEstado'),    
    path('categorias/', CategoriaView.as_view(), name='categoria_list'),
    path('categorias/ver/<int:pk>', CategoriaVer.as_view(), name='categoria_ver'),
    path('categorias/new', CategoriaNew.as_view(), name='categoria_new'),
    path('categorias/edit/<int:pk>', CategoriaEdit.as_view(), name='categoria_edit'),    
    path('categorias/estado/<int:pk>/<estado>', categoriaEstado, name='categoriaEstado'),    
    path('subcategorias/', SubCategoriaView.as_view(), name='subcategoria_list'),
    path('subcategorias/ver/<int:pk>', SubCategoriaVer.as_view(), name='subcategoria_ver'),
    path('subcategorias/new', SubCategoriaNew.as_view(), name='subcategoria_new'),
    path('subcategorias/edit/<int:pk>', SubCategoriaEdit.as_view(), name='subcategoria_edit'),
    path('subcategorias/estado/<int:pk>/<estado>', subcategoriaEstado, name='subcategoriaEstado'),
    path('marcas/', MarcaView.as_view(), name='marca_list'),
    path('marcas/ver/<int:pk>', MarcaVer.as_view(), name='marca_ver'),
    path('marcas/new', MarcaNew.as_view(), name='marca_new'),
    path('marcas/edit/<int:pk>', MarcaEdit.as_view(), name='marca_edit'),    
    path('marcas/estado/<int:pk>/<estado>', marcaEstado, name='marcaEstado'),    
    path('productos/', ProductoView.as_view(), name='producto_list'),
    path('productos/new', ProductoNew.as_view(), name='producto_new'),
    path('productos/ver/<int:pk>', ProductoVer.as_view(), name='producto_ver'),
    path('productos/edit/<int:pk>', ProductoEdit.as_view(), name='producto_edit'),    
    path('productos/estado/<int:pk>/<estado>', productoEstado, name='productoEstado'),    
 
]
