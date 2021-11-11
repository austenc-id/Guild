from data import build
import pickle as file

version = build.version('Rescue Team DX')
# vals = vars(version)
# for item in vals:
#   print(item)
pokedex = version.pokedex
for pokemon in pokedex:
  path = f'storage/pokemon/{pokemon.species}'
  with open(path, 'rb') as pokemon:
    pokemon = file.load(pokemon)
  print(pokemon.species)
  for typing in pokemon.typings:
    print(typing.name)
