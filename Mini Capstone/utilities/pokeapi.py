from requests import get


class api:
  url = 'https://pokeapi.co/api/v2/'
  # keys = ['ability', 'berry', 'berry-firmness', 'berry-flavor', 'characteristic', 'contest-effect', 'contest-type', 'egg-group', 'encounter-condition', 'encounter-condition-value', 'encounter-method', 'evolution-chain', 'evolution-trigger', 'gender', 'generation', 'growth-rate', 'item', 'item-attribute', 'item-category', 'item-fling-effect', 'item-pocket', 'language', 'location', 'location-area', 'machine', 'move', 'move-ailment', 'move-battle-style', 'move-category', 'move-damage-class', 'move-learn-method', 'move-target', 'nature', 'pal-park-area', 'pokeathlon-stat', 'pokedex', 'pokemon', 'pokemon-color', 'pokemon-form', 'pokemon-habitat', 'pokemon-shape', 'pokemon-species', 'region', 'stat', 'super-contest-effect', 'type', 'version', 'version-group']
  
  class pokemon:
    # keys = ['abilities', 'base_experience', 'forms', 'game_indices', 'height', 'held_items', 'id', 'is_default', 'location_area_encounters', 'moves', 'name', 'order', 'past_types', 'species', 'sprites', 'stats', 'types', 'weight']
    def __init__(raw, dexid, species):
      raw.id = dexid
      raw.species = species
      raw.data = raw.request()
      raw.types = raw.data['types']
      raw.abils = raw.data['abilities']
      raw.moves = raw.data['moves']
      raw.growth = raw.data['base_experience']
      raw.sprites = raw.data['sprites']
      raw.stats = raw.data['stats']
      raw.weight = raw.data['weight']
    def request(raw):
      url = api.url + f'pokemon/{raw.id}'
      print(url)
      data = get(url)
      data = data.json()
      return data
    def typing(raw):
      typings = []
      for typing in raw.types:
        # keys = ['slot', 'type']
        typing = typing['type']
        # keys = ['name', 'url']
        typing = typing['name']
        typings.append(typing)
      return typings
    def abilities(raw):
      abilities = []
      for abil in raw.abils:
        # keys = ['ability', 'is_hidden', 'slot']
        hidden = abil['is_hidden']
        if hidden != True:
          abil = abil['ability']
          # keys = ['name', 'url']
          abil = abil['name']
          abilities.append(abil)
      return abilities
    def moveset(raw):
      moveset = []
      for move in raw.moves:
        # keys = ['move', 'version_group_details']
        move = move['move']
        # keys = ['name', 'url']
        move = move['name']
        moveset.append(move)
      return moveset

  