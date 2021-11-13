class poke:
  def species(data):
    species = data.capitalize()
    return species

  def typing(data):
    if len(data) == 1:
      typing = f'a {data[0].name} type pokemon'
    elif len(data) == 2:
      typing = f'a {data[0].name} and {data[1].name} type pokemon'
    return typing

  def abilities(data):
    if len(data) == 1:
      abilities = f'ability: {data[0].name}'
    elif len(data) == 2:
      abilities = f'abilities: {data[0].name} or {data[1].name}'
    return abilities

  def print(data):
      species = poke.species(data.species)
      typing = poke.typing(data.typings)
      abilities = poke.abilities(data.abilities)
      print('\n', species)
      print('', typing)
      print('', abilities, '\n')
      return

  def printtyping(data):
    import os
    import pickle as files
    path = 'storage/typings'
    resistvals = {}
    typings = os.listdir(path)
    for typing in typings:
      with open(f'{path}/{typing}', 'rb') as typing:
        typing = files.load(typing)
        resistvals.update({typing.name: 1})
    for typing in data.typings:
      for immunity in typing.immunities:
        resistvals[immunity] *= 0
      for resist in typing.resistances:
        resistvals[resist] *= 0.5
      for weak in typing.weaknesses:
        resistvals[weak] *= 2
    for ability in data.abilities:
      if ability.name == 'levitate':
        resistvals['ground'] *= 0
    immune = []
    vresist = []
    nresist = []
    nweak = []
    vweak = []
    for typing in resistvals:
      value = resistvals[typing]
      if value == 0:
        immune.append(typing)
      elif value == 0.25:
        vresist.append(typing)
      elif value == 0.5:
        nresist.append(typing)
      elif value == 2:
        nweak.append(typing)
      elif value == 4:
        vweak.append(typing)
    species = poke.species(data.species)
    print()
    if len(immune) > 0:
      string = f'{species} is immune to '
      if len(immune) == 1:
          string += immune[0]
      elif len(immune) == 2:
          string += immune[0] + ' and ' + immune[1]
      while len(immune) > 3:
        popimmune = immune.pop()
        string += popimmune + ', '
      if len(immune) == 3:
          string += immune[0] + ', ' + immune[1] + ', and ' + immune[2]
      string += ' type attacks.'
      print(string)
      print()
    else:
      print(f'{species} has no immunities.')
    if len(vresist) > 0:
      string = f'{species} is very resistant to '
      if len(vresist) == 1:
          string += vresist[0]
      elif len(vresist) == 2:
          string += vresist[0] + ' and ' + vresist[1]
      while len(vresist) > 3:
        popresist = vresist.pop()
        string += popresist + ', '
      if len(vresist) == 3:
          string += vresist[0] + ', ' + vresist[1] + ', and ' + vresist[2]
      string += ' type attacks.'
      print(string)
      print()
    if len(nresist) > 0:
      string = f'{species} is resistant to '
      if len(nresist) == 1:
          string += nresist[0]
      elif len(nresist) == 2:
          string += nresist[0] + ' and ' + nresist[1]
      while len(nresist) > 3:
        popresist = nresist.pop()
        string += popresist + ', '
      if len(nresist) == 3:
          string += nresist[0] + ', ' + nresist[1] + ', and ' + nresist[2]
      string += ' type attacks.'
      print(string)
      print()
    if len(nweak) > 0:
      string = f'{species} is weak to '
      if len(nweak) == 1:
          string += nweak[0]
      elif len(nweak) == 2:
          string += nweak[0] + ' and ' + nweak[1]
      while len(nweak) > 3:
        popweak = nweak.pop()
        string += popweak + ', '
      if len(nweak) == 3:
          string += nweak[0] + ', ' + nweak[1] + ', and ' + nweak[2]
      string += ' type attacks.'
      print(string)
      print()
    if len(vweak) > 0:
      string = f'{species} is very weak to '
      if len(vweak) == 1:
          string += vweak[0]
      elif len(vweak) == 2:
          string += vweak[0] + ' and ' + vweak[1]
      while len(vweak) > 3:
        popweak = vweak.pop()
        string += popweak + ', '
      if len(vweak) == 3:
          string += vweak[0] + ', ' + vweak[1] + ', and ' + vweak[2]
      string += ' type attacks.'
      print(string)
      print()
    return

  def printability(data):
    ability = data.name
    description = data.description
    ability = f'\n   {ability} - {description}\n'
    print(ability)
    return
