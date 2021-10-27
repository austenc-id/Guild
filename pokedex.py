class Pokedex:
  
  from utilities.pokefiles import pokefiles
  lists = pokefiles.initialize.all()
  pokelist = lists[0]
  abilitylist = lists[1]
  ptypelist = lists[2]
  
  def build():
    from data.models import dex_models
    pokedex = []
    abilitydex = []
    qualitydex = []
    ptypedex = []
    for ability in Pokedex.abilitylist:
      ability = dex_models.model.Ability(ability)
      if ability.category == 'ability':
        abilitydex.append(ability)
      else:
        qualitydex.append(ability)
    for ptype in Pokedex.ptypelist:
      ptype = dex_models.model.pType(ptype)
      ptypedex.append(ptype)
    for pokemon in Pokedex.pokelist:
      ptypes = []
      for ptype in pokemon['typing']:
        for entry in ptypedex:
          if ptype == entry.name:
            ptype = entry
            ptypes.append(ptype)
      pokemon.update({'typing': ptypes})
      abilities = []
      for ability in pokemon['abilities']:
        for entry in abilitydex:
          if ability == entry.name:
            ability = entry
            abilities.append(ability)
      pokemon.update({'abilities': abilities})
      pokemon = dex_models.model.Pokemon(pokemon)
      pokedex.append(pokemon)
    pokedex.append(qualitydex)
    return pokedex