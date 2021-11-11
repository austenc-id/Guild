from tools.pokeapi import request
from models.typing import Typing
from models.pokemon import Pokemon
from models.ability import Ability


class data:
    def pokemon(dex):
        pokemondata = []
        pokedex = []
        for dexid in dex:
            pokemon = request.pokemon(dexid)
            print(f'requesting {dexid} of {len(dex)}')
            pokemondata.append(pokemon)
        for pokemon in pokemondata:
            dexid = pokemon['id']
            species = pokemon['name']
            typings = pokemon['types']
            formatted = []
            for typing in typings:
              typing = typing['type']
              name = typing['name']
              url = typing['url']
              typing = data.typing(name, url)
              formatted.append(typing)
            typings = formatted
            abilities = pokemon['abilities']
            formatted = []
            for ability in abilities:
              if ability['is_hidden'] == False:
                ability = ability['ability']
                name = ability['name']
                url = ability['url']
                ability = data.ability(name, url)
                formatted.append(ability)
            abilities = formatted
            pokemon = {'dexid': dexid, 'species': species,
                       'typings': typings, 'abilities': abilities}
            pokemon = Pokemon(pokemon)
            pokedex.append(pokemon)
        return pokedex

    def typing(name, url):
        typingdata = request.typing(url)
        interactions = typingdata['damage_relations']
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
        return typing

    def ability(name, url):
      abilitydata = request.ability(url)
      description = abilitydata['flavor_text_entries']
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
      return ability
