from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="API CRUD de Pokemon")


class Caracteristicas(BaseModel):
    peso: float
    altura: float
    fuerza: int
    edad: int


class PokemonBase(BaseModel):
    nombre: str
    imagen: str
    caracteristicas: Caracteristicas
    habilidades: list[str]
    tipo: str
    habitat: str


class PokemonCrear(PokemonBase):
    pass


class Pokemon(PokemonBase):
    id: int


pokemons: dict[int, Pokemon] = {}
proximo_id = 1


def obtener_pokemon_o_error(id: int) -> Pokemon:
    pokemon = pokemons.get(id)
    if pokemon is None:
        raise HTTPException(status_code=404, detail="Pokemon no encontrado")
    return pokemon


@app.get("/pokemons", response_model=list[Pokemon])
async def obtener_pokemons():
    return list(pokemons.values())


@app.post("/pokemons", response_model=Pokemon, status_code=201)
async def crear_pokemon(pokemon: PokemonCrear):
    global proximo_id

    nuevo_pokemon = Pokemon(id=proximo_id, **pokemon.model_dump())
    pokemons[proximo_id] = nuevo_pokemon
    proximo_id += 1

    return nuevo_pokemon


@app.get("/pokemons/{id}", response_model=Pokemon)
async def obtener_pokemon(id: int):
    return obtener_pokemon_o_error(id)


@app.put("/pokemons/{id}", response_model=Pokemon)
async def actualizar_pokemon(id: int, pokemon: PokemonCrear):
    obtener_pokemon_o_error(id)

    pokemon_actualizado = Pokemon(id=id, **pokemon.model_dump())
    pokemons[id] = pokemon_actualizado

    return pokemon_actualizado


@app.delete("/pokemons/{id}")
async def eliminar_pokemon(id: int):
    obtener_pokemon_o_error(id)
    del pokemons[id]

    return {"mensaje": "Pokemon eliminado correctamente"}
