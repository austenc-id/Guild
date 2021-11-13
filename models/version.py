class generations:
  one = [1, 25]


class DX:
  gens = [generations.one]
  dexids = []
  for gen in gens:
    start = gen[0]
    end = gen[1]
    current = start
    while current <= end:
      dexids.append(current)
      current += 1


class Version:
  def __init__(version, data):
    version.name = data['name']
    version.dexids = data['dexids']
    version.gens = data['generations']
    version.pokedex = data['pokedex']
