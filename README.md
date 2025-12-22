# Sistema de Préstamo de Equipos Electrónicos  
Programación Orientada a Objetos (POO) – Python

## Descripción general  
En esta carpeta se presenta un programa desarrollado en Python que aplica los
principios de la Programación Orientada a Objetos (POO) mediante un ejemplo del
mundo real: un sistema de préstamo de equipos electrónicos.

Este programa simula cómo una institución puede registrar usuarios, administrar
equipos y controlar su préstamo y devolución de manera ordenada y comprensible.

---

## Estructura del proyecto  
El proyecto fue organizado en carpetas para facilitar la lectura y el orden del
código:

- **modelos/**
  - `equipo.py`: contiene la clase `Equipo`, que representa los equipos electrónicos
    disponibles para préstamo.
  - `usuario.py`: contiene la clase `Usuario`, que representa a las personas que
    solicitan los equipos.
- **servicios/**
  - `inventario.py`: se encarga de gestionar el inventario y controlar el préstamo
    y la devolución de los equipos.
- **main.py**
  - Archivo principal donde se ejecuta el programa y se muestra el menú interactivo.

Esta organización permite separar responsabilidades y hace que el programa sea más
fácil de entender y mantener.

---

## Funcionamiento del programa  
Al iniciar el programa, se solicita al usuario ingresar su nombre y su número de
cédula.  
Posteriormente, se muestra un menú con las siguientes opciones:

1. Prestar equipo  
2. Devolver equipo  
3. Salir  

El inventario contiene equipos electrónicos identificados por un nombre y un
código único.  
Cuando el usuario selecciona la opción de préstamo, el sistema verifica si el
equipo está disponible. Si lo está, se registra el préstamo correctamente; caso
contrario, se informa que el equipo ya se encuentra prestado.

En la opción de devolución, el sistema permite cambiar el estado del equipo para
que vuelva a estar disponible.  
El menú se repite hasta que el usuario decide salir del programa.

---

## Conceptos de Programación Orientada a Objetos aplicados  
En este proyecto se aplican los siguientes conceptos de POO:

- **Clases y objetos**: se utilizan las clases `Equipo`, `Usuario` e `Inventario`.
- **Encapsulamiento**: cada clase gestiona sus propios atributos y métodos.
- **Interacción entre objetos**: los usuarios interactúan con los equipos a través
  del inventario.
- **Modularidad**: el código se encuentra dividido en módulos para una mejor
  organización.

---

## Conclusión  
Este sistema de préstamo de equipos electrónicos demuestra cómo la Programación
Orientada a Objetos nos permite modelar situaciones reales de forma clara y ordenada.
La estructura utilizada facilita el aprendizaje y muestra una aplicación práctica
de POO.
