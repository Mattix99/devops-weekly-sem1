# API CRUD de Pokemon

Mini proyecto FastAPI 

## Requisitos

- Python 3.10 o mas

## Crear y activar entorno virtual

```powershell
python -m venv .venv
.venv\Scripts\Activate
```

## Instalar dependencias

```powershell
pip install -r requirements.txt
```

## Ejecutar la API

```powershell
uvicorn main:app --reload o al boton de RUN
```

La documentacion automatica de FastAPI queda disponible en:

http://127.0.0.1:8000/docs

Desde aca se va a poder gestionar los endpoints de la API

## Rutas

- `GET /pokemons`: devuelve todos los Pokemon almacenados.
- `POST /pokemons`: crea un Pokemon nuevo.
- `GET /pokemons/{id}`: devuelve el Pokemon correspondiente al ID indicado.
- `PUT /pokemons/{id}`: actualiza el Pokemon correspondiente al ID indicado.
- `DELETE /pokemons/{id}`: elimina el Pokemon correspondiente al ID indicado.

## Ejemplo para crear un Pokemon

`POST /pokemons`

```json
{
  "nombre": "Pikachu",
  "imagen": "https://link_a_imagen_de_pikachu.jpg",
  "caracteristicas": {
    "peso": 6.0,
    "altura": 0.4,
    "fuerza": 55,
    "edad": 5
  },
  "habilidades": [
    "Impactrueno",
    "Cola ferrea"
  ],
  "tipo": "Electrico",
  "habitat": "Bosques"
}
```


## Ejemplo para actualizar un Pokemon

`PUT /pokemons/1`

```json
{
  "nombre": "Pikachu",
  "imagen": "https://link_a_imagen_de_pikachu_actualizada.jpg",
  "caracteristicas": {
    "peso": 6.2,
    "altura": 0.4,
    "fuerza": 60,
    "edad": 6
  },
  "habilidades": [
    "Impactrueno",
    "Ataque rapido"
  ],
  "tipo": "Electrico",
  "habitat": "Bosques"
}
```

## Ejemplos de uso

Obtener todos los Pokemon:

```http
GET http://127.0.0.1:8000/pokemons
Accept: application/json
```

Obtener un Pokemon por ID:

```http
GET http://127.0.0.1:8000/pokemons/1
Accept: application/json
```

Eliminar un Pokemon por ID:

```http
DELETE http://127.0.0.1:8000/pokemons/1
Accept: application/json
```

## Almacenamiento en memoria

Los Pokemon se guardan en un diccionario de Python llamado `pokemons`, usando el ID como clave. La variable `proximo_id` comienza en `1` y aumenta cada vez que se crea un Pokemon nuevo.

## Consultar la lista de pokemons para saber el id
