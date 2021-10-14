
# Consumo de PokeApi con FastAPI
Por: Leonardo Patiño Rodriguez
<div align="center">
	<img height="200" src="https://leoesleoesleo.github.io/imagenes/fastapi_pokeapi.png" alt="PokeAPI">
</div>  

## &nbsp; [![pyVersion37](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/download/releases/3.7/)

## Manual de instalación

### Características
<p align="justify">
Características habituales proporcionadas por FastAPI:
Basado en estándares abiertos
OpenAPI para la creación de APIs, incluyendo declaraciones de path operations, parámetros, body requests, seguridad, etc.
Documentación automática del modelo de datos con JSON Schema (dado que OpenAPI mismo está basado en JSON Schema).
Diseñado alrededor de estos estándares después de un estudio meticuloso. En vez de ser una capa añadida a último momento.
Esto también permite la generación automática de código de cliente para muchos lenguajes.
</p>
<p align="justify">
PokeAPI proporciona una interfaz API RESTful para objetos altamente detallados creados a partir de miles de líneas de datos relacionados con Pokémon.
Se Cubre específicamente la franquicia de videojuegos. Al usar PokeAPI, puedes consumir información sobre Pokémon, sus movimientos, habilidades, tipos,
grupos de huevos y mucho, mucho más.
</p>

### Pasos

- Clonar repositorio
  ```
  git clone https://github.com/leoesleoesleo/poke_fastapi.git
  ```
- Crear entorno virtual

    Ejemplo anaconda
   ```
   conda create -n fastapiPokeapi python=3.7.9 
   ```
   ```
   conda activate fastapiPokeapi
   ```

- Navegar hasta la carpeta del proyecto para instalar dependencias
    ```
    pip install -r requirements.txt
    ```
- Validar cobertura de la aplicación  
    ```
  coverage run -m pytest -v -p no:cacheprovider --junitxml=junit/test-results.xml --cov=. --cov-report=xml --cov-report=html
    ```

- Iniciar programa
    ```
    uvicorn main:app --host="0.0.0.0" --port="5000" --reload
    ```
    ```sh
    127.0.0.1:5000
    ```

## MANUAL TÉCNICO

### Contexto

<p align="justify">
  Exponer un servicio web cuyo único parámetro es el "nombre" de una búsqueda
  de Pokémon. Este servicio no debe hacer una solicitud hacia PokeApi. 
  La respuesta debe incluir la siguiente información:
  -Detalles de Pokémon disponibles
  -Incluir para todas las evoluciones relacionadas
  -Tipo de evolución (prevolución / evolución)
  -Identificación
  -Nombre.
</p>
