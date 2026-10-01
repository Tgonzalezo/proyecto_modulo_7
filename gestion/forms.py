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

        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el apellido'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'correo@ejemplo.com'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el teléfono'
                }
            ),
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

        widgets = {
            'cliente': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'numero_cuenta': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ejemplo: 101001'
                }
            ),
            'tipo_cuenta': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'saldo': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el saldo inicial'
                }
            ),
            'activa': forms.CheckboxInput(
                attrs={
                    'class': 'custom-control-input'
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['cliente'].empty_label = 'Seleccione una opción'

        opciones_tipo_cuenta = [
            ('', 'Seleccione una opción')
        ] + list(self.fields['tipo_cuenta'].choices)[1:]

        self.fields['tipo_cuenta'].choices = opciones_tipo_cuenta


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

        widgets = {
            'cuenta': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'tipo': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'monto': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el monto'
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3,
                    'placeholder': 'Ingrese una descripción'
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['cuenta'].empty_label = 'Seleccione una opción'

        opciones_tipo = [
            ('', 'Seleccione una opción')
        ] + list(self.fields['tipo'].choices)[1:]

        self.fields['tipo'].choices = opciones_tipo