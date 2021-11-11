class Pokemon:
  def __init__(pokemon, data):
    pokemon.dexid = data['dexid']
    pokemon.species = data['species']
    pokemon.typings = data['typings']
    pokemon.abilities = data['abilities']
