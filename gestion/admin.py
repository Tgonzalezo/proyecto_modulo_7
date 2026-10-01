from django.contrib import admin
from .models import Cliente, Cuenta, Transaccion, Beneficiario


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'apellido',
        'email',
        'telefono',
        'usuario',
        'fecha_creacion'
    )

    search_fields = (
        'nombre',
        'apellido',
        'email'
    )


@admin.register(Beneficiario)
class BeneficiarioAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'email'
    )

    search_fields = (
        'nombre',
        'email'
    )

    filter_horizontal = (
        'clientes',
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
        'cliente__nombre',
        'cliente__apellido'
    )

    list_filter = (
        'tipo_cuenta',
        'activa'
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

    search_fields = (
        'cuenta__numero_cuenta',
        'descripcion'
    )