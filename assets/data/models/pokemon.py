class Pokemon:
  def __init__(pokemon, data):
    pokemon.dexid = data['dexid']
    pokemon.species = data['species']
    pokemon.typing = data['typing']
    pokemon.abilities = data['abilities']
    pokemon.moveset = data['moveset']
    # pokemon.immune = data['immune']
    # pokemon.quarter = data['quarter']
    # pokemon.half = data['half']
    # pokemon.double = data['double']
    # pokemon.quadruple = data['quadruple']
