from data import data
from models import version


DXdex = version.DX.dexids
start = 1
end = 386
pokedex = data.pokemon(DXdex)
for pokemon in pokedex:
  print(pokemon.species)
  for typing in pokemon.typings:
    print(typing.name)
  for ability in pokemon.abilities:
    print(ability.name)
    print(ability.description)
