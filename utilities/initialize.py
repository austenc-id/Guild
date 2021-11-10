from data.pokefiles import pokefiles
from utilities.pokeapi import typing as api


class initialize:
  # > 3 read/load all data in storage and return tuple of lists
  def all():
    # > 4 create a list from each file
    pokelist = initialize.pokemon()
    abilitylist = initialize.abilities()
    qualitylist = initialize.qualities()
    typelist = api.getdata()
    # > 5 ask user to add new data then add that data to the correct list
    addnew = input('would you like to add new data?\n')
    if addnew == 'yes':
      newdata = initialize.new()
      for pokemon in newdata[0]:
        pokelist.append(pokemon)
      for ability in newdata[1]:
        abilitylist.append(ability)
      for quality in newdata[2]:
        qualitylist.append(quality)
    initialize.write(
        [pokelist, abilitylist, qualitylist, typelist])
    return pokelist, abilitylist, qualitylist, typelist

  def new():
    from data.models import POKEMON, ABILITY, QUALITY
    from utilities.responses import response
    options = ['pokemon', 'ability', 'quality', 'quit']
    # * 1 ask user to add new data and to specify what data model to use
    addnew = input(f'add new\n{options}\n')
    # * 2 call the responses module to check input against provided options and return the matched option (or the original input if no match found)
    addnew = response.validate.selection(addnew, options)
    pokelist = []
    abilitylist = []
    qualitylist = []
    # * 3 loop until user enters "quit" asking for new data and adding it to the correct list
    while addnew != options[3]:
      if addnew == options[0]:
        newdata = POKEMON.Pokemon.new()
        # ! issue with loop not breaking
        for pokemon in newdata:
          pokelist.append(pokemon)
      elif addnew == options[1]:
        newdata = ABILITY.Ability.new()
        for ability in newdata:
          abilitylist.append(ability)
      elif addnew == options[2]:
        newdata = QUALITY.Quality.new()
        for quality in newdata:
          qualitylist.append(quality)
        addnew = input(f'add new\n{options}\n')
        addnew = response.validate.selection(addnew, options)
    return pokelist, abilitylist, qualitylist

  def write(lists):
    pokefiles.pokemon.write(lists[0])
    pokefiles.abilities.write(lists[1])
    pokefiles.qualities.write(lists[2])
    pokefiles.typing.write(lists[3])

  def pokemon():
    pokelist = []
    file = pokefiles.pokemon.read()
    for pokemon in file:
      pokelist.append(pokemon)
    return pokelist

  def abilities():
    abilitylist = []
    file = pokefiles.abilities.read()
    for ability in file:
      abilitylist.append(ability)
    return abilitylist

  def qualities():
    qualitylist = []
    file = pokefiles.qualities.read()
    for quality in file:
      qualitylist.append(quality)
    return qualitylist

  def types():
    typelist = []
    file = pokefiles.typing.read()
    for type in file:
      typelist.append(type)
    return typelist
