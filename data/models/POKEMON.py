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

  def new():
    from utilities.responses import response
    addnew = input('add new pokemon?\n')
    data = []
    while addnew not in response.polar.valid:
      addnew = input('add new pokemon?\n')
    while addnew in response.polar.yes:
      dexid = input('species id: ')
      while True:
        try:
          int(dexid)
        except:
          dexid = input('species id: ')
        else:
          dexid = int(dexid)
          break
      species = input('species: ')
      typing = input('typing: ')
      typing = typing.split()
      abilities = input('ability name: ')
      abilities = abilities.split(',')
      pokemon = {'id': dexid, 'species': species,
                 'typing': typing, 'abilities': abilities}
      data.append(pokemon)
      addnew = input('add new pokemon?\n')
    return data
