class pokefiles:
    import os
    path = os.getcwd()

    class pokemon:

        def readfile():
            import json
            file = open(f'{pokefiles.path}\\data\\storage\\pokemon.json')
            file = file.read()
            file = json.loads(file)
            file.sort(key=lambda pokemon: pokemon['id'])
            return file

        def writefile(pokelist):
            import json
            pokelist.sort(key=lambda pokemon: pokemon['id'])
            pokelist = json.dumps(pokelist)
            file = open(f'{pokefiles.path}\\data\\storage\\pokemon.json', 'w')
            file.write(pokelist)

    class abilities:

        def readfile():
            import json
            file = open(f'{pokefiles.path}\\data\\storage\\abilities.json')
            file = file.read()
            file = json.loads(file)
            file.sort(key=lambda ability: (ability['name']))
            return file

        def writefile(abilitylist):
            import json
            abilitylist.sort(key=lambda ability: (ability['name']))
            abilitylist = json.dumps(abilitylist)
            file = open(
                f'{pokefiles.path}\\data\\storage\\abilities.json', 'w')
            file.write(abilitylist)

    class qualities:

        def readfile():
            import json
            file = open(f'{pokefiles.path}\\data\\storage\\qualities.json')
            file = file.read()
            file = json.loads(file)
            file.sort(key=lambda quality: (quality['name']))
            return file

        def writefile(qualitylist):
            import json
            qualitylist.sort(key=lambda quality: (quality['name']))
            qualitylist = json.dumps(qualitylist)
            file = open(
                f'{pokefiles.path}\\data\\storage\\qualities.json', 'w')
            file.write(qualitylist)

    class Types:

        def readfile():
            import json
            file = open(f'{pokefiles.path}\\data\\storage\\types.json')
            file = file.read()
            file = json.loads(file)
            file.sort(key=lambda type: type['name'])
            return file

        def writefile(typelist):
            import json
            typelist.sort(key=lambda type: type['name'])
            typelist = json.dumps(typelist)
            file = open(f'{pokefiles.path}\\data\\storage\\types.json', 'w')
            file.write(typelist)

    class initialize:

        def all():
            pokelist = pokefiles.initialize.pokemon()
            abilitylist = pokefiles.initialize.abilities()
            qualitylist = pokefiles.initialize.qualities()
            typelist = pokefiles.initialize.types()
            newdata = pokefiles.initialize.new()
            for pokemon in newdata[0]:
              pokelist.append(pokemon)
            for ability in newdata[1]:
              abilitylist.append(ability)
            for quality in newdata[2]:
              qualitylist.append(quality)
            for type in newdata[3]:
              typelist.append(type)
            pokefiles.initialize.write(
                [pokelist, abilitylist, qualitylist, typelist])
            return pokelist, abilitylist, qualitylist, typelist

        def new():
          from data.models import POKEMON, ABILITY, QUALITY, TYPE
          from utilities.responses import response
          options = ['pokemon', 'ability', 'quality', 'type', 'quit']
          addnew = input(f'add new\n{options}\n')
          addnew = response.validate.selection(addnew, options)
          pokelist = []
          abilitylist = []
          qualitylist = []
          typelist = []
          while addnew != options[4]:
            if addnew == options[0]:
              newdata = POKEMON.Pokemon.new()
              for pokemon in newdata:
                pokelist.append(pokemon)
            elif addnew == options[1]:
              newdata = ABILITY.Ability.new()
              for ability in newdata:
                abilitylist.append(ability)
            elif addnew == options[2]:
              newdata = QUALITY.Quality.new()
              for quality in newdata:
                  qualitylist.append(quality)
            elif addnew == options[3]:
              newdata = TYPE.Type.new()
              for type in newdata:
                  typelist.append(type)
            addnew = input(f'add new\n{options}\n')
            addnew = response.validate.selection(addnew, options)
          return pokelist, abilitylist, qualitylist, typelist

        def write(lists):
          pokefiles.pokemon.writefile(lists[0])
          pokefiles.abilities.writefile(lists[1])
          pokefiles.qualities.writefile(lists[2])
          pokefiles.Types.writefile(lists[3])

        def pokemon():
            pokelist = []
            file = pokefiles.pokemon.readfile()
            for pokemon in file:
                pokelist.append(pokemon)

            return pokelist

        def abilities():
            abilitylist = []
            file = pokefiles.abilities.readfile()
            for ability in file:
                abilitylist.append(ability)
            return abilitylist

        def qualities():
            qualitylist = []
            file = pokefiles.qualities.readfile()
            for quality in file:
                qualitylist.append(quality)

            return qualitylist

        def types():
            typelist = []
            file = pokefiles.Types.readfile()
            for type in file:
                typelist.append(type)
            return typelist
