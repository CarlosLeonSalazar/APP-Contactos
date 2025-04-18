APP CONTACTOS


	La siguiente es una aplicación de contactos realizada con Python, la cual se ejecuta desde la línea de comandos con el módulo argparse. Es un ejercicio realizado por mi en el contexto de un curso de Python Avanzado.

Versión de python: 3.12.5

Módulos:
	-argparse
	-re
	-json
	-sys

* no librerías externas

	La aplicación de contactos contiene las siguientes funcionalidades:

Crear un contacto
Buscar un contacto
Mostrar la lista de contactos
Eliminar un contacto

Resultado:

Genera archivo .json como atributo de clase

*Nota : Los datos en el archivo .jason son datos ficticios, a modo de ejemplo


Estructura:

contactos_app/
│
├── contactos/                  # Paquete principal (con la lógica de la app)
│   ├── __init__.py
│   ├── modelos.py              # Clases como Contactos, GestorContactos
│   └── funciones.py            # Funciones auxiliares -Validaciones
│
├── app_contactos.py           # Script principal (entrada de la app con argparse)
├── requirements.txt           # Dependencias (puede estar vacío)
├── README.md                  # Descripción del proyecto
├── contactos.json             # Archivo donde se almacenan los contactos

