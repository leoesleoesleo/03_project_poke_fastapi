from fastapi import FastAPI
from pokeapi import generate_structure_api

app = FastAPI()

@app.get("/pokemon/{pokemon}")
async def main(pokemon='bulbasaur'):
    """
    Shoot Process
    """
    json = generate_structure_api(poke=pokemon)
    return json
