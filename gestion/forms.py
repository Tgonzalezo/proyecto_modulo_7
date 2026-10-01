from django import forms
from .models import Cliente, Cuenta, Transaccion


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = [
            'nombre',
            'apellido',
            'email',
            'telefono'
        ]

        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'email': 'Correo electrónico',
            'telefono': 'Teléfono'
        }


class CuentaForm(forms.ModelForm):

    class Meta:
        model = Cuenta
        fields = [
            'cliente',
            'numero_cuenta',
            'tipo_cuenta',
            'saldo',
            'activa'
        ]

        labels = {
            'cliente': 'Cliente',
            'numero_cuenta': 'Número de cuenta',
            'tipo_cuenta': 'Tipo de cuenta',
            'saldo': 'Saldo disponible',
            'activa': 'Cuenta activa'
        }


class TransaccionForm(forms.ModelForm):

    class Meta:
        model = Transaccion
        fields = [
            'cuenta',
            'tipo',
            'monto',
            'descripcion'
        ]

        labels = {
            'cuenta': 'Cuenta',
            'tipo': 'Tipo de transacción',
            'monto': 'Monto',
            'descripcion': 'Descripción'
        }