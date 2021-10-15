
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

### Respuesta
Ejemplo con el pokemon bulbasaur
```Javascript
	{
		"id": [
			1
		],
		"name": [
			"bulbasaur"
		],
		"detail": {
			"pokeslot": [
				1
			],
			"poketype": [
				"grass"
			],
			"pokeversion": [
				"red-blue"
			],
			"base_happiness": [
				70
			],
			"capture_rate": [
				45
			],
			"color": [
				"green"
			],
			"v_egg_groups": [
				"monster",
				"plant"
			]
		},
		"list_evolution": [
			"ivysaur",
			"venusaur"
		],
		"evolution": "ivysaur",
		"prevolution": ""
	}
```

### Fuentes de datos

Se consume los siguientes servicios de PokeAPI.  
```
'https://pokeapi.co/api/v2/evolution-chain/'
'https://pokeapi.co/api/v2/pokemon-form/'
'https://pokeapi.co/api/v2/pokemon-species/'
```

Y se evidencian las siguientes relaciones:
<div align="center">
	<img height="200" src="https://leoesleoesleo.github.io/imagenes/diangrama_relacional_poke_fastapi.PNG" alt="PokeAPI">
</div> 

### Arquitectura

Requerimientos no Funcionales
-	Las funciones son recursivas para escalar los datos en caso que el servicio reciba una lista de pokemon.
-	Las pruebas unitarias son escalables – (pytest)
-	La Cobertura del programa llega a un 88% (Coverage)
-	Las Funciones y métodos están comentados
-	El programa proporciona logs de información y errores
-	El programa cuenta con manual de instalación

#### Detalles del desarrollo

<p align="justify">
Se crean 5 funciones recursivas que consumen los servicios y se encargan de retornar los datos en JSON, si no se puede acceder 
al servicio las funciones retornan las listas vacias.
<ul>
	<li><strong>list_evolution()</strong> Consume el servicio de evolution-chain y retorna dos listas, la primera es la lista de los nombres 
		de los pokemon y la segunda otra lista con las evoluciones relacionadas. 
	</li>
	<li><strong>list_form_pokemon()</strong> Consume el servicio de pokemon-form y retorna 3 listas con: slot, type, version respectivamente.
		Estos datos hacen parte de los detalles de los pokemon. 
	</li>
	<li><strong>list_evolution_species()</strong> Consume el servicio de pokemon-species, esta funcion relaciona la api de pokemon-form con 
		la cadena de evolución mediante la api de especies de pokemon para consultar sus evoluciones, consulta también algunos detalles
		de los pokémon, retorna 5 listas y un entero : base_happiness, capture_rate, color, egg_groups, id_pokemon y el id para buscar 
		la evolución.
		Estos datos también hacen parte de los detalles de los pokemon. 
	</li>
	<li><strong>evolution_prevolution()</strong> Este no consume ningún servicio porque recibe los datos para asignar la evolución y 
		prevolución del pokemon enviado como parametro, retorna 2 cadenas : evolution y prevolution. 
	</li>
	<li><strong>generate_structure_api()</strong> Este no consume ningún servicio pero si utiliza las funciones descritas anteriormete para
		armar y generar el JSON de salida. 
	</li>
</ul>	
</p>

## Cobertura

<p align="center">
  <a href="#"><img src="https://leoesleoesleo.github.io/imagenes/covertura_pokeapi.PNG"></a>
</p>
