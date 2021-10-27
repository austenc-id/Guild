class model:
  
  class Team:
    
    def __init__(team, name, members):
      team.name = name
      team.members = members
    def add(pokedex, qualitydex):
      name = input('team name: ')
      members = []
      while len(members) < 3:
        member = model.Member.add(pokedex, qualitydex)
        members.append(member['name'])
      team = {'name': name, 'members': members}
      return team, members
      
  class Member:
      
    def __init__(member, data):
      member.name = data['name']
      member.species = data['species'].species
      member.typing = []
      for ptype in data['species'].typing:
        member.typing.append(ptype.name)
      member.role = data
      member.ability = data['ability']
      member.quality = data['quality']
    def add(pokedex, qualitydex):
      name = input('name: ')
      species = input('species: ')
      member_ability = input('ability: ')
      quality = input('quality: ')
      for pokemon in pokedex:
        if species == pokemon.species:
          species = pokemon
          for ability in species.abilities:
            if member_ability == ability.name:
              member_ability = ability
      for ability in qualitydex:
        if quality == ability.name:
          quality = ability
      member = {'name': name,'species': species.species, 'ability': member_ability.name, 'quality': quality.name}
      return member