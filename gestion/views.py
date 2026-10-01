from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Cliente, Cuenta, Transaccion
from .forms import ClienteForm, CuentaForm, TransaccionForm


# ==========================
# CLIENTES
# ==========================

class ClienteListView(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'gestion/clientes/lista.html'
    context_object_name = 'clientes'


class ClienteCreateView(LoginRequiredMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'gestion/clientes/formulario.html'
    success_url = reverse_lazy('clientes')


class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'gestion/clientes/formulario.html'
    success_url = reverse_lazy('clientes')


class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = 'gestion/clientes/eliminar.html'
    success_url = reverse_lazy('clientes')


# ==========================
# CUENTAS
# ==========================

class CuentaListView(LoginRequiredMixin, ListView):
    model = Cuenta
    template_name = 'gestion/cuentas/lista.html'
    context_object_name = 'cuentas'


class CuentaCreateView(LoginRequiredMixin, CreateView):
    model = Cuenta
    form_class = CuentaForm
    template_name = 'gestion/cuentas/formulario.html'
    success_url = reverse_lazy('cuentas')


class CuentaUpdateView(LoginRequiredMixin, UpdateView):
    model = Cuenta
    form_class = CuentaForm
    template_name = 'gestion/cuentas/formulario.html'
    success_url = reverse_lazy('cuentas')


class CuentaDeleteView(LoginRequiredMixin, DeleteView):
    model = Cuenta
    template_name = 'gestion/cuentas/eliminar.html'
    success_url = reverse_lazy('cuentas')


# ==========================
# TRANSACCIONES
# ==========================

class TransaccionListView(LoginRequiredMixin, ListView):
    model = Transaccion
    template_name = 'gestion/transacciones/lista.html'
    context_object_name = 'transacciones'


class TransaccionCreateView(LoginRequiredMixin, CreateView):
    model = Transaccion
    form_class = TransaccionForm
    template_name = 'gestion/transacciones/formulario.html'
    success_url = reverse_lazy('transacciones')


class TransaccionUpdateView(LoginRequiredMixin, UpdateView):
    model = Transaccion
    form_class = TransaccionForm
    template_name = 'gestion/transacciones/formulario.html'
    success_url = reverse_lazy('transacciones')


class TransaccionDeleteView(LoginRequiredMixin, DeleteView):
    model = Transaccion
    template_name = 'gestion/transacciones/eliminar.html'
    success_url = reverse_lazy('transacciones')