from data import build
import pickle as files
from tools.pokeformat import poke
import os


class MysteonDex:
  def __init__(dex, name):
    dex.name = name

  def build(dex):
    version = build.version(dex.name)
    pokedex = version.pokedex
    return pokedex

  def run(dex, pokedex):
    options = ['search', 'all', 'done']
    option = input(f'Which pokemon would you like to see? \n  {options}\n')
    while option != 'done':
      if option == 'all':
        for pokemon in pokedex:
          path = f'storage/pokemon/{pokemon.dexid}'
          with open(path, 'rb') as pokemon:
            pokemon = files.load(pokemon)
            poke.print(pokemon)
      elif option == 'search':
        find = input('enter the name of the pokemon: ')
        for pokemon in pokedex:
          if find == pokemon.species:
            found = pokemon
            break
        poke.print(found)
        details = ['typing', 'abilities', 'no']
        detail = input(
              f'Would you like to check this pokemon\'s details? \n   {details}\n enter option from the above list: ')
        while detail != 'no':
          if detail == 'typing':
              poke.printtyping(found)
          elif detail == 'abilities':
              species = poke.species(found.species)
              print(f'\n   {species}\'s abilities: ')
              for ability in found.abilities:
                poke.printability(ability)
          detail = input(
                f'Would you like to check this pokemon\'s details? \n   {details}\n enter option from list: ')
        else:
          print('pokemon not found')
      option = input(f'Which pokemon would you like to see? \n  {options}\n')


versions = ['Rescue Team DX']
version = input(f'What version would you like to run?\n   {versions}\n')
DXdex = MysteonDex('Rescue Team DX')
pokedex = DXdex.build()
DXdex.run(pokedex)
