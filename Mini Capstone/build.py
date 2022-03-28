import os, json
from assets.utilities.pokeapi import api
from assets.data.models.pokemon import Pokemon
class Version:
    def __init__(dex, name):
        dex.basepath = "assets/data/storage/json/"
        dex.name = name
        dex.version = dex.getversion()
        dex.pokemon = dex.version['pokemon']
        dex.pokedex = []
    def getversion(dex):
        versionpath = f"{dex.basepath}versions/{dex.name}.json"
        if os.path.exists(versionpath):
            with open(versionpath) as file:
                file = file.read()
                version = json.loads(file)
        return version
    def getpokemon(dex):
        count = 1
        for pokemon in dex.pokemon:
            dexid = pokemon['dexid']
            species = pokemon['species']
            path = f"{dex.basepath}pokemon/{species}.json"
            with open(path) as file:
                file = file.read()
                pokemon = json.loads(file)
            try:
                typing = pokemon['typing']
                abilities = pokemon['abilities']
                moveset = pokemon['moveset']
            except:
                stop = len(dex.pokemon)
                # stop = 9
                if count <= stop:
                    data = api.pokemon(dexid, species)
                    print(f'requesting {count} of {stop}')
                    typing = data.typing()
                    abilities = data.abilities()
                    moveset = data.moveset()
                    pokemon.update({'typing': typing, 'abilities': abilities, 'moveset': moveset})
                    pokemon = json.dumps(pokemon)
                    with open(path, 'w') as file:
                        file.write(pokemon)
                    count += 1
                else:
                    break
            else:
                pokemon = Pokemon(pokemon)
                dex.pokedex.append(pokemon)
        return
