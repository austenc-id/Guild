class Pokemon:
  def __init__(pokemon, data):
    pokemon.dexid = data['dexid']
    pokemon.species = data['species']
    pokemon.typings = data['typings']
    pokemon.abilities = data['abilities']
    pokemon.immune = data['immune']
    pokemon.quarter = data['quarter']
    pokemon.half = data['half']
    pokemon.double = data['double']
    pokemon.quadruple = data['quadruple']
