# Trabajo Práctico 2: Programación Dinámica For The Win

TP2 de la materia: Teoría de Algoritmos.

## Integrantes

- Denise Dall'Acqua - 108645
- Martin Alejo Polese - 106808
- Nicolas Agustin Riedel - 102130

## Informe

El informe del trabajo se encuentra [acá](./Informe.pdf).

## Ejecución

Para correr el programa, se debe ejecutar el siguiente comando sobre el directorio raíz:

```python3 main.py <path>```

Donde **path** es la ruta a un archivo csv, cuya primer linea tiene las monedas de la fila separadas por `;`.

***Ejemplo***: ```python3 main.py ./ejemplos/20.txt```

## Tests

Para correr las pruebas, ejecutar el comando ```pytest``` sobre el directorio raíz.

***Nota**: Se debe contar con pytest instalado.*

## Notebook para verificar complejidad algorítmica
* Navegar al directorio `/VerificacionComplejidad`
* Instalar el paquete python3-venv (si no está instalado): `sudo apt install python3-venv`
* Crear el entorno virtual: `python3 -m venv myenv`
* Iniciar el venv: `source myenv/bin/activate`
* Instalar dependencias necesarias con: `pip install -r requirements.txt`
* Lanzar Jupyter notebook con: `jupyter notebook`

Al finalizar, para desactivar el entorno virtual: `deactivate`