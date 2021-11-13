from data import build
import pickle as files
from tools.stringify import stringify
import os

version = build.version('Rescue Team DX')
pokedex = version.pokedex
options = ['search', 'all', 'done']
option = input(f'Which pokemon would you like to see? \n  {options}\n')
while option != 'done':
  if option == 'all':
    for pokemon in pokedex:
      path = f'storage/pokemon/{pokemon.dexid}'
      with open(path, 'rb') as pokemon:
        pokemon = files.load(pokemon)
        stringify.print(pokemon)
  elif option == 'search':
    find = input('enter the name of the pokemon: ')
    for pokemon in pokedex:
      if find == pokemon.species:
        find = pokemon.dexid
    path = f'storage/pokemon/{find}'
    if os.path.exists(path):
      with open(path, 'rb') as found:
        pokemon = files.load(found)
        stringify.print(pokemon)
      details = ['typing', 'abilities', 'no']
      detail = input(
          f'Would you like to check this pokemon\'s details? \n   {details}\n enter option from above list: ')
      while detail != 'no':
        if detail == 'typing':
          stringify.printtyping(pokemon)
        elif detail == 'abilities':
          for ability in pokemon.abilities:
            stringify.printability(ability)
        detail = input(
            f'Would you like to check this pokemon\'s details? \n   {details}\n enter option from list: ')
    else:
      print('pokemon not found')
  option = input(f'Which pokemon would you like to see? \n  {options}\n')
