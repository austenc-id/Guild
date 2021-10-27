class model:
  class Pokemon:
    def __init__(pokemon, data):
      pokemon.id = data['id']
      pokemon.species = data['species']
      pokemon.typing = data['typing']
      pokemon.abilities = data['abilities']
      pokemon.stats = data
      pokemon.moves = data
      pokemon.locations = data
      pokemon.evolutions = data
    def add():
      from utilities.responses import response
      addnew = input('add new pokemon?\n')
      data = []
      while addnew not in response.polar.valid:
        addnew = input('add new pokemon?\n')
      while addnew in response.polar.yes:
        dexid = input('pokemon id: ')
        dexid = int(dexid)
        species = input('species: ')
        typing = input('typing: ')
        typing = typing.split()
        count = input('how many abilities: ')
        count = int(count)
        abilities = []
        if len(abilities) < count:
          ability = input('ability name: ')
          abilities.append(ability)
        pokemon = {'id': dexid, 'species': species, 'typing': typing, 'abilities': abilities}
        data.append(pokemon)
        addnew = input('add new pokemon?\n')
      return data
  class Ability:
    def __init__(ability, data):
      ability.name = data['name']
      ability.effect = data['effect']
      ability.conditions = data['conditions']
      ability.category = data['type']
    def add():
      from utilities.responses import response
      addnew = input('add new ability?\n')
      data = []
      while addnew not in response.polar.valid:
        addnew = input('add new ability?\n')
      while addnew in response.polar.yes:
        name = input('ability name: ')
        effect = input('ability effect: ')
        conditional = input('are there conditions to this effect?\n')
        conditions = ''
        if conditional in response.polar.yes:
          conditions += input('conditions: ')
        category = input('ability or quality: ')
        ability = {'name': name, 'effect': effect, 'conditions': conditions, 'type': category}
        data.append(ability)
        addnew = input('add new ability?\n')
      return data
  class pType:
    def __init__(pType, data):
      pType.name = data['name']
      pType.interactions = data
    def add():
      from utilities.responses import response
      addnew = input('add new type?\n')
      data = []
      while addnew not in response.polar.valid:
        addnew = input('add new type?\n')
      while addnew in response.polar.yes:
        name = input('type name: ')
        immunity = input('What is this type immune to?\n')
        immunity = immunity.split()
        resists = input('What types does this type resist?\n')
        resists = resists.split()
        weakness = input('What types is this type weak to?\n')
        weakness = weakness.split()
        defensive = {'immune': immunity, 'resist': resists, 'weak': weakness}
        immunity = input('What types are immune to this type?\n')
        immunity = immunity.split()
        resists = input('What types resist this type?\n')
        resists = resists.split()
        weakness = input('What types are weak to this type?\n')
        weakness = weakness.split()
        offensive = {'immune': immunity, 'resist': resists, 'weak': weakness}
        interactions = {'defensive': defensive, 'offensive': offensive}
        ptype = {'name': name, 'interactions': interactions}
        data.append(ptype)
        addnew = input('add new type?\n')
      return data