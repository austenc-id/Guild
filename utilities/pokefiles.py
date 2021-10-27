class pokefiles:
  
  class pokemon:
    
    def readfile():
      import json
      file = open('X:\\dungeon-dex\\data\\pokemon.json')
      file = file.read()
      file = json.loads(file)
      file.sort(key=lambda pokemon: pokemon['id'])
      return file
    
    def writefile(pokelist):
      import json
      pokelist.sort(key=lambda pokemon: pokemon['id'])
      pokelist = json.dumps(pokelist)
      file = open('X:\\dungeon-dex\\data\\pokemon.json', 'w')
      file.write(pokelist)
      
  class abilities:
    
    def readfile():
      import json
      file = open('X:\\dungeon-dex\\data\\abilities.json')
      file = file.read()
      file = json.loads(file)
      file.sort(key=lambda ability: (ability['type'], ability['name']))
      return file
    
    def writefile(abilitylist):
      import json
      abilitylist.sort(key=lambda ability: (ability['type'], ability['name']))
      abilitylist = json.dumps(abilitylist)
      file = open('X:\\dungeon-dex\\data\\abilities.json', 'w')
      file.write(abilitylist)
      
  class pTypes:
    
    def readfile():
      import json
      file = open('X:\\dungeon-dex\\data\\ptypes.json')
      file = file.read()
      file = json.loads(file)
      file.sort(key=lambda ptype: ptype['name'])
      return file
    
    def writefile(ptypelist):
      import json
      ptypelist.sort(key=lambda ptype: ptype['name'])
      ptypelist = json.dumps(ptypelist)
      file = open('X:\\dungeon-dex\\data\\ptypes.json', 'w')
      file.write(ptypelist)
      
  class initialize:
    
    def all():
      pokelist = pokefiles.initialize.pokemon()
      abilitylist = pokefiles.initialize.abilities()
      ptypelist = pokefiles.initialize.ptypes()
      return pokelist, abilitylist, ptypelist
    
    def pokemon():
      from data.models import dex_models
      pokelist = []
      file = pokefiles.pokemon.readfile()
      for pokemon in file:
        pokelist.append(pokemon)
      newdata = dex_models.model.Pokemon.add()
      for pokemon in newdata:
        pokelist.append(pokemon)
      pokefiles.pokemon.writefile(pokelist)
      return pokelist

    def abilities():
      from data.models import dex_models
      abilitylist = []
      file = pokefiles.abilities.readfile()
      for ability in file:
        abilitylist.append(ability)
      newdata = dex_models.model.Ability.add()
      for ability in newdata:
        abilitylist.append(ability)
      pokefiles.abilities.writefile(abilitylist)
      return abilitylist

    def ptypes():
      from data.models import dex_models
      ptypelist = []
      file = pokefiles.pTypes.readfile()
      for ptype in file:
        ptypelist.append(ptype)
      newdata = dex_models.model.pType.add()
      for ptype in newdata:
        ptypelist.append(ptype)
      pokefiles.pTypes.writefile(ptypelist)
      return ptypelist