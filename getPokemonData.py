import json
import pokebase as pb

def getPokemonByName(name: str):
    with open("data/pokemon.json", mode="r", encoding="utf-8") as pokemon_file:
        pokemon_registry = json.load(pokemon_file)

    for pokemon in pokemon_registry:
        if pokemon['Name'] == name:
            return pokemon