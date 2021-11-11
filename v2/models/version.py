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
