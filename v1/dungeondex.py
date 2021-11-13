class Dungeondex:
    from utilities.initialize import initialize
    # > 2 call the initialize model to get lists
    lists = initialize.all()
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
        # > 6 loop through each list item to create a python object using the corresponding model then add it to the appropriate support dex
        for ability in Dungeondex.abilitylist:
            ability = ABILITY.Ability(ability)
            abilitydex.append(ability)
        for quality in Dungeondex.qualitylist:
            quality = QUALITY.Quality(quality)
            qualitydex.append(quality)
        for typing in Dungeondex.typelist:
            typing = TYPE.Typing(typing)
            typedex.append(typing)
        # > 7 loop through each pokemon attribute and support dex to assign the appropriate objects to the pokemon before adding it to the pokedex
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
        # pokedex.append(qualitydex)
        return pokedex


# > 1 initializes the application and returns the dungeondex
dungeondex = Dungeondex.build()
options = ['show all', 'search', 'done']
action = input(f'what would you like to do?\n{options}\n')
while action != 'done':
  if action == 'show all':
    for pokemon in dungeondex:
      print(pokemon.species)
  elif action == 'search':
    find = input('enter the pokemon\'s name: ')
    for pokemon in dungeondex:
      if find == pokemon.species:
        found = pokemon
        break
    vals = vars(found)
    exclude = ['typing', 'multipliers', 'resistances']
    for item in vals:
      if item == 'species':
        print(vals[item])
      elif item == 'typing':
        count = len(pokemon.typing)
        typings = 'a '
        for typing in pokemon.typing:
          typing = typing.name
          typings += typing
          if count == 1:
            typings += ' type.'
          else:
            typings += ' and '
            count -= 1
        print(typings)
      elif item == 'zero':
        print(f'immune to: {vals[item]} type attacks.')
  action = input(f'what would you like to do?\n{options}\n')
