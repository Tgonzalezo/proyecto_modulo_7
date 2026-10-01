from django.db import models
from django.contrib.auth.models import User


class Cliente(models.Model):
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    nombre = models.CharField(
        max_length=100
    )

    apellido = models.CharField(
        max_length=100
    )

    email = models.EmailField(
        unique=True
    )

    telefono = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Beneficiario(models.Model):
    nombre = models.CharField(
        max_length=100
    )

    email = models.EmailField()

    clientes = models.ManyToManyField(
        Cliente,
        related_name='beneficiarios',
        blank=True
    )

    def __str__(self):
        return self.nombre


class Cuenta(models.Model):

    TIPOS_CUENTA = [
        ('VISTA', 'Cuenta Vista'),
        ('AHORRO', 'Cuenta de Ahorro'),
    ]

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='cuentas'
    )

    numero_cuenta = models.CharField(
        max_length=20,
        unique=True
    )

    tipo_cuenta = models.CharField(
        max_length=20,
        choices=TIPOS_CUENTA
    )

    saldo = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    activa = models.BooleanField(
        default=True
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.numero_cuenta} - {self.cliente}"


class Transaccion(models.Model):

    TIPOS_TRANSACCION = [
        ('DEPOSITO', 'Depósito'),
        ('RETIRO', 'Retiro'),
        ('TRANSFERENCIA', 'Transferencia'),
    ]

    cuenta = models.ForeignKey(
        Cuenta,
        on_delete=models.CASCADE,
        related_name='transacciones'
    )

    tipo = models.CharField(
        max_length=20,
        choices=TIPOS_TRANSACCION
    )

    monto = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    descripcion = models.CharField(
        max_length=255,
        blank=True
    )

    fecha = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.tipo} - ${self.monto}"