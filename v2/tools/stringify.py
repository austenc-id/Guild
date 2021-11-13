class stringify:
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
      species = stringify.species(data.species)
      typing = stringify.typing(data.typings)
      abilities = stringify.abilities(data.abilities)
      print('\n', species)
      print('', typing)
      print('', abilities, '\n')
      return

  def printtyping(data):
    print('feature coming soon')
    return

  def printability(data):
    ability = data.name
    description = data.description
    ability = f'\n{ability} - {description}\n'
    print(ability)
    return
