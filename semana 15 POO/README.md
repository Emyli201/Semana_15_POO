# Restaurante App — Semana 15

Sistema de gestión para un restaurante desarrollado en Python con Tkinter, aplicando los principios de Programación Orientada a Objetos (POO). En esta semana se incorpora la gestión de ventas, que relaciona usuarios y productos mediante un flujo básico de manejo de eventos.

## Propósito de la Semana 15

El objetivo de esta semana es comprender los conceptos fundamentales del manejo de eventos en Tkinter. Para ello, se utiliza la operación de venta como contexto práctico: una acción del usuario (hacer clic en un botón) inicia una respuesta en la aplicación a través de un callback, que delega la operación al servicio correspondiente y muestra el resultado en la interfaz.

## Evolución sobre el proyecto anterior

Partiendo de la versión construida en semanas anteriores, se conservan el inicio de sesión, la navegación, la gestión de productos y la consulta de usuarios. Sobre esta base se incorpora:

- Una nueva sección de Ventas dentro de la interfaz principal.
- El modelo Venta, que representa la relación entre un usuario, un producto y la fecha de la operación.
- La persistencia de ventas mediante el archivo ventas.json.
- La selección de un usuario y un producto existentes mediante componentes de Tkinter/ttk.
- Un botón "Registrar venta" asociado a un método mediante command=.
- Un callback de venta que obtiene las selecciones de la interfaz, solicita la operación a RestauranteServicio, actualiza la vista y comunica el resultado al usuario.
- La presentación de las ventas registradas en una tabla Treeview.

## Flujo de manejo de eventos

La sección de Ventas demuestra el fundamento de manejo de eventos trabajado en la semana:

USUARIO
   ↓
realiza una acción (hacer clic en "Registrar venta")
   ↓
BOTÓN / COMPONENTE
   ↓
command= (asociado al método registrar_venta)
   ↓
CALLBACK (obtiene las selecciones de la interfaz)
   ↓
RestauranteServicio (valida y registra la venta)
   ↓
PERSISTENCIA (ventas.json)
   ↓
RESPUESTA EN LA INTERFAZ (actualización de la tabla y mensaje)

Este flujo permite reconocer cómo una acción del usuario inicia una respuesta en la aplicación sin concentrar toda la lógica dentro de la interfaz. Las validaciones, reglas y persistencia de la venta se mantienen en RestauranteServicio.

## Estructura del proyecto

restaurante_app/
├── assets/
│   └── iconos/
│       ├── cerrar.png
│       ├── inicio.png
│       ├── logo.png
│       ├── productos.png
│       ├── registrar.png
│       ├── usuario.png
│       └── ventas.png
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── main.py
└── README.md

## Persistencia de datos

La aplicación guarda y lee la información desde tres archivos JSON en la carpeta datos/:

- usuarios.json: credenciales y datos de los usuarios.
- productos.json: catálogo de productos del restaurante.
- ventas.json: registro histórico de ventas.

Cada vez que se registra una venta, el servicio guarda automáticamente el cambio en ventas.json. Al cerrar y volver a ejecutar la aplicación, las ventas registradas se recuperan correctamente.

## Arquitectura y principios POO

El proyecto sigue una arquitectura modular con separación de responsabilidades:

- modelos/: define las clases del dominio (Producto, Usuario, Venta).
- servicios/: contiene la lógica de negocio (RestauranteServicio) y el acceso a archivos (ArchivoServicio).
- ui/: contiene las vistas de la interfaz gráfica (LoginView y MainView).
- datos/: almacena la persistencia en archivos JSON.
- assets/: contiene los íconos y el logo del sistema.
- main.py: punto de entrada que coordina las vistas y el servicio.

Principios aplicados:

- Encapsulamiento: cada clase expone solo lo necesario mediante métodos.
- Abstracción: los servicios ocultan los detalles de implementación a la interfaz.
- Separación de responsabilidades: la interfaz no accede directamente a los archivos; lo hace a través del servicio.
- Reutilización: los modelos representan entidades claras y reutilizables.

## Requisitos previos

- Python 3.8 o superior instalado en el sistema.
- Tkinter incluido (viene por defecto con la instalación estándar de Python en Windows).
- No se requieren dependencias externas adicionales.

## Instalación y ejecución

1. Clona o descarga el proyecto en tu equipo.
2. Abre una terminal (CMD o PowerShell) y navega hasta la carpeta del proyecto:

cd restaurante_app

3. Ejecuta la aplicación:

py main.py

o si usas Python directamente:

python main.py

## Credenciales de acceso

La aplicación incluye dos usuarios de ejemplo almacenados en datos/usuarios.json:

- Usuario: dayan, Contraseña: 1234, Rol: Administrador
- Usuario: antonio, Contraseña: 1234, Rol: Cajero

Nota: las contraseñas se muestran aquí con fines académicos. En una versión real deberían almacenarse cifradas.

## Uso de la aplicación

1. Iniciar sesión con las credenciales indicadas.
2. En el menú lateral podrás navegar entre:
   - Inicio: panel con el resumen general.
   - Usuarios: consulta de los usuarios registrados.
   - Productos: registro, actualización, búsqueda y eliminación de productos.
   - Ventas: selección de un usuario y un producto para registrar una venta, y consulta de las ventas registradas.
   - Cerrar sesión: vuelve a la pantalla de login.

## Comprobación de funcionamiento

- La aplicación inicia sin errores.
- El inicio de sesión y la navegación existente continúan funcionando.
- Las secciones de Usuarios y Productos mantienen sus funciones.
- Existe una sección visible de Ventas.
- Se puede seleccionar un usuario y un producto registrados.
- El botón "Registrar venta" utiliza command= para ejecutar el callback.
- El callback delega el registro a RestauranteServicio.
- La nueva venta se almacena en ventas.json.
- La venta aparece en la tabla de la interfaz.
- Al cerrar y volver a ejecutar, las ventas se recuperan correctamente.

## Autor

Emyli Dayanna Moran Cruz

Proyecto académico desarrollado para la asignatura de Programación Orientada a Objetos, Semana 15.
