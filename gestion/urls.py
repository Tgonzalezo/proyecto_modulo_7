from django.urls import path

from .views import (
    ClienteListView,
    ClienteCreateView,
    ClienteUpdateView,
    ClienteDeleteView,
    CuentaListView,
    CuentaCreateView,
    TransaccionListView,
    TransaccionCreateView,
)


urlpatterns = [

    # Clientes
    path(
        'clientes/',
        ClienteListView.as_view(),
        name='clientes'
    ),

    path(
        'clientes/nuevo/',
        ClienteCreateView.as_view(),
        name='crear_cliente'
    ),

    path(
        'clientes/editar/<int:pk>/',
        ClienteUpdateView.as_view(),
        name='editar_cliente'
    ),

    path(
        'clientes/eliminar/<int:pk>/',
        ClienteDeleteView.as_view(),
        name='eliminar_cliente'
    ),


    # Cuentas
    path(
        'cuentas/',
        CuentaListView.as_view(),
        name='cuentas'
    ),

    path(
        'cuentas/nueva/',
        CuentaCreateView.as_view(),
        name='crear_cuenta'
    ),


    # Transacciones
    path(
        'transacciones/',
        TransaccionListView.as_view(),
        name='transacciones'
    ),

    path(
        'transacciones/nueva/',
        TransaccionCreateView.as_view(),
        name='crear_transaccion'
    ),
]