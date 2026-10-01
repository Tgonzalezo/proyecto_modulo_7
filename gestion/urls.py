from django.urls import path

from .views import (
    ClienteListView,
    ClienteCreateView,
    ClienteUpdateView,
    ClienteDeleteView,
    CuentaListView,
    CuentaCreateView,
    CuentaUpdateView,
    CuentaDeleteView,
    TransaccionListView,
    TransaccionCreateView,
    TransaccionUpdateView,
    TransaccionDeleteView,
)


urlpatterns = [

    # CLIENTES
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


    # CUENTAS
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

    path(
        'cuentas/editar/<int:pk>/',
        CuentaUpdateView.as_view(),
        name='editar_cuenta'
    ),

    path(
        'cuentas/eliminar/<int:pk>/',
        CuentaDeleteView.as_view(),
        name='eliminar_cuenta'
    ),


    # TRANSACCIONES
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

    path(
        'transacciones/editar/<int:pk>/',
        TransaccionUpdateView.as_view(),
        name='editar_transaccion'
    ),

    path(
        'transacciones/eliminar/<int:pk>/',
        TransaccionDeleteView.as_view(),
        name='eliminar_transaccion'
    ),
]