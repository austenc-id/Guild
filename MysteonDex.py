# class containing the entire MysteonDex
class MysteonDex:
  def __init__(dex, name):
    # name used to build desired version
    dex.name = name
  # method to build instantiated MysteonDex
  def build(dex):
    # import project module designed to parse and build all data
    from data import build
    version = build.version(dex.name)
    pokedex = version.pokedex
    # pokedex to be used in the main run() method
    return pokedex
  # method to run the MysteonDex
  def run(dex, pokedex):
    # import python lib to save python objects without conversion to/from string formats
    import pickle as files
    # import project module to format and return strings from data
    from tools.pokeformat import poke
    # current ui options available
    options = ['search', 'all', 'done']
    option = input(f'Which pokemon would you like to see? \n  {options}\n')
    # REPL to contiously allow the user to display all or searched pokemon
    while option != 'done':
      # prints a basic entry for each pokemon
      if option == 'all':
        for pokemon in pokedex:
          # path where 'pickled' file is stored for each pokemon
          path = f'storage/pokemon/{pokemon.dexid}'
          with open(path, 'rb') as pokemon:
            # load the file with the pickle lib
            pokemon = files.load(pokemon)
            poke.print(pokemon)
      # allows user to search for a specific pokemon, prints a basic entry, then allows the user to select details to print
      elif option == 'search':
        find = input('enter the name of the pokemon: ')
        # loop through pokedex and break when user input == pokemon species
        for pokemon in pokedex:
          if find == pokemon.species:
            found = pokemon
            break
        poke.print(found)
        # current details available
        details = ['typing', 'abilities', 'no']
        detail = input(
              f'Would you like to check this pokemon\'s details? \n   {details}\n enter option from the above list: ')
        # REPL allowing the user to continuosly check each detail entry without having to search for the same pokemon again
        while detail != 'no':
          # print typing details
          if detail == 'typing':
              poke.printtyping(found)
          # print ability descriptions
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

# instantiate class for use in the terminal
versions = ['Rescue Team DX']
# ask for version (only 1 option available and is therfore hardcoded making this a placeholder for when additional versions are made available)
version = input(f'What version would you like to run?\n   {versions}\n')
DXdex = MysteonDex('Rescue Team DX')
pokedex = DXdex.build()
DXdex.run(pokedex)
