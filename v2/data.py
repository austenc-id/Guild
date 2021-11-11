from os import fspath
from tools.pokeapi import request
from models.typing import Typing
from models.pokemon import Pokemon
from models.ability import Ability
from models.version import Version
from models.generation import Generation as Gen


class build:

    def version(name):
        from json import loads
        import pickle as save
        path = 'storage/versions.json'
        file = open(path).read()
        data = loads(file)
        dexids = []
        generations = []
        for entry in data:
            if entry['name'] == name:
                version = entry
                break
        gens = version['generations']
        for gen in gens:
            if gen['ids'] == 'all':
                gen = build.generation(gen['name'])
                generations.append(gen)
        version.update({'generations': generations})
        for gen in generations:
            start = gen.start
            while start <= gen.end:
                dexids.append(start)
                start += 1
        version.update({'dexids': dexids})
        pokedex = build.pokedex(dexids)
        version.update({'pokedex': pokedex})
        version = Version(version)
        return version

    def generation(genid):
        from json import loads
        path = 'storage/generations.json'
        file = open(path).read()
        data = loads(file)
        for entry in data:
            if entry['name'] == int(genid):
                gen = Gen(entry)
                return gen

    def pokedex(dexids):
        import pickle as files
        import os
        pokedex = []
        for dexid in dexids:
            pokemon = request.pokemon(dexid)
            print(f'loading {dexid} of {len(dexids)}')
            species = pokemon['name']
            path = f'storage/pokemon/{species}'
            if os.path.exists(path):
              with open(path, 'rb') as file:
                  pokemon = files.load(file)
                  pokedex.append(pokemon)
            else:
              print(f'requesting {dexid} of {len(dexids)}')
              dexid = pokemon['id']
              typings = pokemon['types']
              formatted = []
              for typing in typings:
                  typing = typing['type']
                  name = typing['name']
                  url = typing['url']
                  typing = build.typing(name, url)
                  formatted.append(typing)
              typings = formatted
              abilities = pokemon['abilities']
              formatted = []
              for ability in abilities:
                  if ability['is_hidden'] == False:
                      ability = ability['ability']
                      name = ability['name']
                      url = ability['url']
                      ability = build.ability(name, url)
                      formatted.append(ability)
              abilities = formatted
              pokemon = {'dexid': dexid, 'species': species,
                         'typings': typings, 'abilities': abilities}
              pokemon = Pokemon(pokemon)
              path = f'storage/pokemon/{pokemon.species}'
              if os.path.exists(path):
                with open(path, 'wb') as file:
                    files.dump(pokemon, file)
              else:
                with open(path, 'w') as file:
                  file.write('')
                with open(path, 'wb') as file:
                    files.dump(pokemon, file)
              pokedex.append(pokemon)
        return pokedex

    def typing(name, url):
        import pickle as files
        import os
        path = f'storage/typings/{name}'
        if os.path.exists(path):
          with open(path, 'rb') as file:
            typing = files.load(file)
        else:
          data = request.typing(url)
          interactions = data['damage_relations']
          immunities = []
          resistances = []
          weaknesses = []
          data = interactions['no_damage_from']
          for immunity in data:
              immunity = immunity['name']
              immunities.append(immunity)
          data = interactions['half_damage_from']
          for resist in data:
              resist = resist['name']
              resistances.append(resist)
          data = interactions['double_damage_from']
          for weakness in data:
              weakness = weakness['name']
              weaknesses.append(weakness)
          typing = {'name': name, 'zero': immunities,
                    'half': resistances, 'double': weaknesses}
          typing = Typing(typing)
          if os.path.exists(path):
            with open(path, 'wb') as file:
              files.dump(typing, file)
          else:
            with open(path, 'w') as file:
              file.write('')
            with open(path, 'wb') as file:
              files.dump(typing, file)
        return typing

    def ability(name, url):
        import pickle as files
        import os
        path = f'storage/abilities/{name}'
        if os.path.exists(path):
          with open(path, 'rb') as file:
            ability = files.load(file)
        else:
          data = request.ability(url)
          description = data['flavor_text_entries']
          entry = description.pop()
          language = entry['language']
          language = language['name']
          while language != 'en':
              entry = description.pop()
              language = entry['language']
              language = language['name']
          entry = entry['flavor_text']
          ability = {'name': name, 'effect': entry}
          ability = Ability(ability)
          if os.path.exists(path):
            with open(path, 'wb') as file:
              files.dump(ability, file)
          else:
            with open(path, 'w') as file:
              file.write('')
            with open(path, 'wb') as file:
              files.dump(ability, file)
        return ability
