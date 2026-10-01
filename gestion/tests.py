from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Cliente, Cuenta, Transaccion


class ModelosTest(TestCase):

    def setUp(self):
        self.cliente = Cliente.objects.create(
            nombre='Ana',
            apellido='Gonzalez',
            email='ana@test.com',
            telefono='123456789'
        )

        self.cuenta = Cuenta.objects.create(
            cliente=self.cliente,
            numero_cuenta='100001',
            tipo_cuenta='VISTA',
            saldo=500000,
            activa=True
        )

        self.transaccion = Transaccion.objects.create(
            cuenta=self.cuenta,
            tipo='DEPOSITO',
            monto=30000,
            descripcion='Depósito de prueba'
        )

    def test_creacion_cliente(self):
        self.assertEqual(self.cliente.nombre, 'Ana')
        self.assertEqual(self.cliente.email, 'ana@test.com')

    def test_relacion_cliente_cuenta(self):
        self.assertEqual(self.cuenta.cliente, self.cliente)

    def test_relacion_cuenta_transaccion(self):
        self.assertEqual(self.transaccion.cuenta, self.cuenta)

    def test_saldo_cuenta(self):
        self.assertEqual(self.cuenta.saldo, 500000)


class VistasTest(TestCase):

    def setUp(self):
        self.usuario = User.objects.create_user(
            username='usuario_prueba',
            password='clave12345'
        )

        self.cliente = Cliente.objects.create(
            nombre='Luis',
            apellido='Perez',
            email='luis@test.com',
            telefono='987654321'
        )

    def test_login_requerido_clientes(self):
        response = self.client.get(reverse('clientes'))
        self.assertEqual(response.status_code, 302)

    def test_lista_clientes_autenticado(self):
        self.client.login(
            username='usuario_prueba',
            password='clave12345'
        )

        response = self.client.get(reverse('clientes'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Luis')
        self.assertContains(response, 'Perez')

    def test_crear_cliente(self):
        self.client.login(
            username='usuario_prueba',
            password='clave12345'
        )

        response = self.client.post(
            reverse('crear_cliente'),
            {
                'nombre': 'Maria',
                'apellido': 'Lopez',
                'email': 'maria@test.com',
                'telefono': '111111111'
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Cliente.objects.filter(
                email='maria@test.com'
            ).exists()
        )