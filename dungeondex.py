class Dungeondex:
  
  from data.pokefiles import pokefiles
  lists = pokefiles.initialize.all()
  pokelist = lists[0]
  abilitylist = lists[1]
  qualitylist = lists[2]
  typelist = lists[3]
  
  def build():
    from data.models import POKEMON, ABILITY, TYPE, QUALITY
    pokedex = []
    abilitydex = []
    qualitydex = []
    typedex = []
    for ability in Dungeondex.abilitylist:
      ability = ABILITY.Ability(ability)
      abilitydex.append(ability)
    for quality in Dungeondex.qualitylist:
      quality = QUALITY.Quality(quality)
      qualitydex.append(quality)
    for type in Dungeondex.typelist:
      type = TYPE.Type(type)
      typedex.append(type)
    for pokemon in Dungeondex.pokelist:
      types = []
      for type in pokemon['typing']:
        for entry in typedex:
          if type == entry.name:
            type = entry
            types.append(type)
      pokemon.update({'typing': types})
      abilities = []
      for ability in pokemon['abilities']:
        for entry in abilitydex:
          if ability == entry.name:
            ability = entry
            abilities.append(ability)
      pokemon.update({'abilities': abilities})
      pokemon = POKEMON.Pokemon(pokemon)
      pokedex.append(pokemon)
    pokedex.append(qualitydex)
    return pokedex


pokedex = Dungeondex.build()
