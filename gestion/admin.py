from django.contrib import admin
from .models import Cliente, Cuenta, Transaccion


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'apellido',
        'email',
        'telefono',
        'fecha_creacion'
    )

    search_fields = (
        'nombre',
        'apellido',
        'email'
    )


@admin.register(Cuenta)
class CuentaAdmin(admin.ModelAdmin):
    list_display = (
        'numero_cuenta',
        'cliente',
        'tipo_cuenta',
        'saldo',
        'activa'
    )

    search_fields = (
        'numero_cuenta',
        'cliente__nombre'
    )


@admin.register(Transaccion)
class TransaccionAdmin(admin.ModelAdmin):
    list_display = (
        'cuenta',
        'tipo',
        'monto',
        'fecha'
    )

    list_filter = (
        'tipo',
        'fecha'
    )