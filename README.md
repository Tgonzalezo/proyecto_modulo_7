# Alke Wallet

## Descripción del proyecto

Alke Wallet es una aplicación web desarrollada con Django que permite gestionar clientes, cuentas y transacciones financieras mediante una interfaz web.

El proyecto fue desarrollado como parte del Módulo 7 de Desarrollo Web con Django y tiene como objetivo aplicar conceptos relacionados con bases de datos, ORM, migraciones, operaciones CRUD, consultas personalizadas, autenticación, administración, archivos estáticos y pruebas.

La aplicación utiliza SQLite como base de datos durante el desarrollo y está estructurada para permitir una futura adaptación a PostgreSQL en un entorno de producción.

---

## Objetivo

El objetivo de Alke Wallet es desarrollar una aplicación web funcional que permita administrar clientes, cuentas y transacciones financieras de manera organizada y segura.

La aplicación implementa el ORM de Django para acceder y manipular datos, utiliza migraciones para mantener sincronizada la base de datos y emplea funcionalidades integradas de Django para autenticación, administración y archivos estáticos.

---

## Funciones principales

La aplicación permite:

- Registrar clientes.
- Listar clientes.
- Editar clientes.
- Eliminar clientes.
- Registrar cuentas asociadas a clientes.
- Visualizar cuentas.
- Consultar saldos.
- Registrar transacciones.
- Visualizar transacciones.
- Administrar clientes, cuentas y transacciones desde Django Admin.
- Autenticar usuarios mediante inicio y cierre de sesión.
- Proteger vistas para usuarios autenticados.
- Ejecutar consultas mediante el ORM de Django.
- Ejecutar filtros avanzados.
- Realizar agregaciones mediante `annotate()`.
- Ejecutar consultas SQL mediante `raw()`.
- Ejecutar consultas SQL directas mediante cursores.
- Utilizar archivos estáticos para la presentación visual mediante CSS.
- Ejecutar pruebas unitarias y de integración.

---

## Tecnologías utilizadas

- Python 3.12
- Django 6.1.1
- SQLite
- HTML5
- CSS3
- Visual Studio Code
- Git
- GitHub

---

## Estructura del proyecto

La estructura principal del proyecto es la siguiente:

~~~text
alke_wallet/
│
├── alke_wallet/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── gestion/
│   ├── migrations/
│   │
│   ├── static/
│   │   └── gestion/
│   │       └── css/
│   │           └── estilos.css
│   │
│   ├── templates/
│   │   ├── registration/
│   │   │   └── login.html
│   │   │
│   │   └── gestion/
│   │       ├── base.html
│   │       ├── clientes/
│   │       │   ├── lista.html
│   │       │   ├── formulario.html
│   │       │   └── eliminar.html
│   │       ├── cuentas/
│   │       │   ├── lista.html
│   │       │   └── formulario.html
│   │       └── transacciones/
│   │           ├── lista.html
│   │           └── formulario.html
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── db.sqlite3
├── manage.py
├── README.md
├── requirements.txt
└── .gitignore
~~~

---

## Configuración de la base de datos

Durante el desarrollo se utilizó SQLite, base de datos incluida por defecto en Django.

La configuración se encuentra en `alke_wallet/settings.py`.

Ejemplo:

~~~python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
~~~

Para un entorno de producción, la aplicación puede adaptarse para utilizar PostgreSQL modificando la configuración de `DATABASES` e instalando el adaptador correspondiente.

---

## Modelo de datos

El proyecto utiliza tres modelos principales: `Cliente`, `Cuenta` y `Transaccion`.

### Cliente

Representa a una persona registrada en Alke Wallet.

Campos principales:

- nombre
- apellido
- email
- teléfono
- fecha de creación

### Cuenta

Representa una cuenta financiera asociada a un cliente.

Campos principales:

- cliente
- número de cuenta
- tipo de cuenta
- saldo
- estado
- fecha de creación

La relación entre Cliente y Cuenta es de uno a muchos.

~~~text
Cliente 1 ───────── N Cuenta
~~~

### Transacción

Representa un movimiento financiero asociado a una cuenta.

Los tipos de transacción implementados son:

- Depósito
- Retiro
- Transferencia

Campos principales:

- cuenta
- tipo
- monto
- descripción
- fecha

La relación entre Cuenta y Transacción es de uno a muchos.

~~~text
Cuenta 1 ───────── N Transacción
~~~

La estructura general del modelo de datos es:

~~~text
Cliente
   │
   │ 1:N
   ▼
Cuenta
   │
   │ 1:N
   ▼
Transacción
~~~

---

## ORM de Django

La aplicación utiliza el ORM de Django para realizar operaciones sobre la base de datos sin necesidad de utilizar SQL directamente en la mayoría de los casos.

### Obtener todos los clientes

~~~python
Cliente.objects.all()
~~~

### Filtrar clientes cuyo nombre comienza con A

~~~python
Cliente.objects.filter(nombre__istartswith='A')
~~~

### Filtrar cuentas con saldo superior a 100000

~~~python
Cuenta.objects.filter(saldo__gt=100000)
~~~

### Excluir cuentas inactivas

~~~python
Cuenta.objects.exclude(activa=False)
~~~

### Filtrar transacciones por tipo

~~~python
Transaccion.objects.filter(tipo='DEPOSITO')
~~~

---

## Consultas con annotate()

Se utilizó `annotate()` para realizar agregaciones utilizando el ORM.

~~~python
from django.db.models import Count

Cliente.objects.annotate(
    total_cuentas=Count('cuentas')
)
~~~

También se utilizó la siguiente consulta para visualizar el número de cuentas asociadas a cada cliente:

~~~python
for cliente in Cliente.objects.annotate(
    total_cuentas=Count('cuentas')
):
    print(
        cliente.nombre,
        cliente.total_cuentas
    )
~~~

---

## Consultas SQL personalizadas con raw()

Además del ORM, se implementó una consulta SQL personalizada utilizando `raw()`.

~~~python
clientes = Cliente.objects.raw(
    "SELECT * FROM gestion_cliente WHERE telefono IS NOT NULL"
)
~~~

Luego, los resultados pueden recorrerse de la siguiente forma:

~~~python
for cliente in clientes:
    print(
        cliente.nombre,
        cliente.email
    )
~~~

---

## Consultas mediante cursor

También se utilizó una conexión directa a la base de datos mediante cursor.

~~~python
from django.db import connection

with connection.cursor() as cursor:
    cursor.execute(
        "SELECT COUNT(*) FROM gestion_cliente"
    )

    resultado = cursor.fetchone()

    print(
        "Total de clientes:",
        resultado[0]
    )
~~~

---

## Migraciones

Las migraciones permiten mantener sincronizados los modelos de Django con la estructura de la base de datos.

Para generar migraciones:

~~~bash
python manage.py makemigrations
~~~

Para aplicarlas:

~~~bash
python manage.py migrate
~~~

Durante el desarrollo del proyecto se generaron migraciones para:

- Cliente
- Cuenta
- Transacción

Las migraciones se almacenan en `gestion/migrations/`.

---

## Operaciones CRUD

La aplicación implementa operaciones CRUD mediante vistas genéricas de Django.

Las vistas utilizadas son:

~~~python
ListView
CreateView
UpdateView
DeleteView
~~~

### CRUD de Clientes

El módulo de clientes permite:

- Crear clientes.
- Listar clientes.
- Editar clientes.
- Eliminar clientes.

Rutas principales:

~~~text
/clientes/
/clientes/nuevo/
/clientes/editar/<id>/
/clientes/eliminar/<id>/
~~~

### Gestión de Cuentas

El módulo de cuentas permite:

- Crear cuentas.
- Listar cuentas.

Rutas principales:

~~~text
/cuentas/
/cuentas/nueva/
~~~

### Gestión de Transacciones

El módulo de transacciones permite:

- Registrar transacciones.
- Listar transacciones.

Rutas principales:

~~~text
/transacciones/
/transacciones/nueva/
~~~

---

## Formularios

Los formularios se implementaron utilizando `ModelForm`.

Los formularios definidos son:

- `ClienteForm`
- `CuentaForm`
- `TransaccionForm`

Se encuentran en `gestion/forms.py`.

---

## Seguridad CSRF

Todos los formularios utilizan protección CSRF mediante:

~~~html
{% csrf_token %}
~~~

Esta protección se utiliza en formularios de creación, edición, eliminación y cierre de sesión.

---

## Autenticación de usuarios

La aplicación utiliza el sistema de autenticación integrado de Django mediante `django.contrib.auth`.

La página de inicio de sesión se encuentra en:

~~~text
/cuentas/login/
~~~

Las vistas principales se encuentran protegidas mediante:

~~~python
LoginRequiredMixin
~~~

Las redirecciones de autenticación se configuran en `alke_wallet/settings.py`.

~~~python
LOGIN_REDIRECT_URL = '/clientes/'
LOGOUT_REDIRECT_URL = '/cuentas/login/'
LOGIN_URL = '/cuentas/login/'
~~~

---

## Django Admin

Los modelos Cliente, Cuenta y Transacción se encuentran registrados en `gestion/admin.py`.

El panel administrativo está disponible en:

~~~text
http://127.0.0.1:8000/admin/
~~~

Desde allí es posible agregar, modificar, eliminar, buscar y filtrar registros.

---

## Superusuario

Para crear un usuario administrador:

~~~bash
python manage.py createsuperuser
~~~

---

## Archivos estáticos

El proyecto utiliza `django.contrib.staticfiles`.

El archivo CSS principal se encuentra en:

~~~text
gestion/static/gestion/css/estilos.css
~~~

La configuración utilizada es:

~~~python
STATIC_URL = 'static/'
~~~

El CSS se carga desde `base.html` mediante:

~~~html
{% load static %}

<link rel="stylesheet" href="{% static 'gestion/css/estilos.css' %}">
~~~

---

## Plantillas HTML

Las plantillas se encuentran en `gestion/templates/`.

La plantilla principal es:

~~~text
gestion/templates/gestion/base.html
~~~

Las demás páginas heredan de ella mediante:

~~~django
{% extends 'gestion/base.html' %}
~~~

---

## Idioma y zona horaria

La aplicación fue configurada en español:

~~~python
LANGUAGE_CODE = 'es'
~~~

Y con zona horaria de Santiago de Chile:

~~~python
TIME_ZONE = 'America/Santiago'
~~~

---

## Pruebas unitarias y de integración

Las pruebas se implementaron en `gestion/tests.py`.

Se desarrollaron siete pruebas para verificar:

- creación de un cliente;
- relación entre Cliente y Cuenta;
- relación entre Cuenta y Transacción;
- saldo de una cuenta;
- protección del listado de clientes mediante autenticación;
- acceso correcto de usuarios autenticados;
- creación de un cliente mediante formulario.

Para ejecutar las pruebas:

~~~bash
python manage.py test
~~~

Resultado obtenido:

~~~text
Found 7 test(s).

System check identified no issues (0 silenced).

.......

Ran 7 tests in 3.773s

OK
~~~

---

## Instalación del proyecto

### 1. Crear entorno virtual

~~~bash
python -m venv venv
~~~

### 2. Activar entorno virtual

En Windows PowerShell:

~~~powershell
.\venv\Scripts\Activate.ps1
~~~

Si PowerShell bloquea la ejecución de scripts temporalmente:

~~~powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
~~~

### 3. Instalar dependencias

~~~bash
pip install -r requirements.txt
~~~

### 4. Aplicar migraciones

~~~bash
python manage.py migrate
~~~

### 5. Crear superusuario

~~~bash
python manage.py createsuperuser
~~~

### 6. Ejecutar servidor

~~~bash
python manage.py runserver
~~~

---

## Acceso a la aplicación

### Clientes

~~~text
http://127.0.0.1:8000/clientes/
~~~

### Cuentas

~~~text
http://127.0.0.1:8000/cuentas/
~~~

### Transacciones

~~~text
http://127.0.0.1:8000/transacciones/
~~~

### Inicio de sesión

~~~text
http://127.0.0.1:8000/cuentas/login/
~~~

### Administración

~~~text
http://127.0.0.1:8000/admin/
~~~

---

## Ejecución de consultas personalizadas

Para ingresar a la shell de Django:

~~~bash
python manage.py shell
~~~

Importar los modelos:

~~~python
from gestion.models import Cliente, Cuenta, Transaccion
~~~

Desde esta shell se pueden ejecutar las consultas ORM y SQL personalizadas utilizadas en el proyecto.

---

## Evidencias del proyecto

Durante el desarrollo se registraron capturas de:

1. Servidor Django funcionando.
2. Migraciones.
3. Panel de administración.
4. Registro de clientes.
5. Registro de cuentas.
6. Registro de transacciones.
7. CRUD de clientes.
8. Listado de cuentas.
9. Listado de transacciones.
10. Consultas con `filter()` y `exclude()`.
11. Consulta con `annotate()`.
12. Consulta SQL mediante `raw()`.
13. Consulta SQL mediante cursor.
14. Inicio de sesión.
15. Usuario autenticado.
16. Cierre de sesión.
17. Archivos estáticos mediante CSS.
18. Pruebas unitarias y de integración.

---

## Resultados

El proyecto logró integrar correctamente los principales componentes de Django requeridos para el desarrollo de una aplicación web conectada a una base de datos.

Se implementaron modelos mediante ORM, relaciones, migraciones, formularios, vistas, rutas, templates, operaciones CRUD, autenticación, administración, consultas personalizadas, consultas SQL, archivos estáticos y pruebas.

El sistema permite administrar clientes, cuentas y transacciones desde una interfaz web y desde el panel administrativo de Django.

---

## Posibles mejoras futuras

- Actualización y eliminación de cuentas.
- Actualización y eliminación de transacciones.
- Transferencias entre cuentas.
- Actualización automática del saldo después de una transacción.
- Validación de saldo antes de realizar retiros.
- Historial detallado por cuenta.
- Panel principal con resumen de saldo.
- Reportes financieros.
- Exportación de transacciones.
- Perfiles individuales de usuarios.
- PostgreSQL para producción.
- Despliegue en un servidor web.

---

## Conclusión

El desarrollo de Alke Wallet permitió aplicar de manera práctica los principales conceptos del desarrollo web con Django.

La utilización del ORM permitió representar y gestionar los datos mediante los modelos Cliente, Cuenta y Transacción, estableciendo relaciones entre las distintas entidades. Las migraciones permitieron mantener sincronizada la estructura de los modelos con la base de datos SQLite.

La implementación de vistas genéricas y formularios permitió desarrollar operaciones CRUD para los registros principales. A su vez, el sistema de autenticación integrado de Django permitió restringir el acceso a las funcionalidades de la aplicación.

También se implementaron consultas personalizadas utilizando `filter()`, `exclude()` y `annotate()`, además de consultas SQL mediante `raw()` y cursores.

El uso de Django Admin permitió gestionar los registros desde una interfaz administrativa, mientras que los archivos estáticos permitieron incorporar estilos personalizados mediante CSS.

Finalmente, las pruebas unitarias y de integración permitieron verificar el funcionamiento de los principales componentes del sistema.

En conjunto, Alke Wallet constituye una aplicación web funcional que integra acceso a datos, ORM, migraciones, consultas, operaciones CRUD, autenticación, administración y pruebas, sentando una base que puede ampliarse en futuras versiones para incorporar nuevas funcionalidades financieras.
