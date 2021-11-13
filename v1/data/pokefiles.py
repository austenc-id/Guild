class pokefiles:
    import os
    path = os.getcwd()

    class pokemon:

        def read():
            import json
            file = open(f'{pokefiles.path}\\data\\storage\\pokemon.json')
            file = file.read()
            file = json.loads(file)
            file.sort(key=lambda pokemon: pokemon['id'])
            return file

        def write(pokelist):
            import json
            pokelist.sort(key=lambda pokemon: pokemon['id'])
            pokelist = json.dumps(pokelist)
            file = open(f'{pokefiles.path}\\data\\storage\\pokemon.json', 'w')
            file.write(pokelist)

    class abilities:

        def read():
            import json
            file = open(f'{pokefiles.path}\\data\\storage\\abilities.json')
            file = file.read()
            file = json.loads(file)
            file.sort(key=lambda ability: (ability['name']))
            return file

        def write(abilitylist):
            import json
            abilitylist.sort(key=lambda ability: (ability['name']))
            abilitylist = json.dumps(abilitylist)
            file = open(
                f'{pokefiles.path}\\data\\storage\\abilities.json', 'w')
            file.write(abilitylist)

    class qualities:

        def read():
            import json
            file = open(f'{pokefiles.path}\\data\\storage\\qualities.json')
            file = file.read()
            file = json.loads(file)
            file.sort(key=lambda quality: (quality['name']))
            return file

        def write(qualitylist):
            import json
            qualitylist.sort(key=lambda quality: (quality['name']))
            qualitylist = json.dumps(qualitylist)
            file = open(
                f'{pokefiles.path}\\data\\storage\\qualities.json', 'w')
            file.write(qualitylist)

    class typing:

        def read():
            import json
            file = open(f'{pokefiles.path}\\data\\storage\\typing.json')
            file = file.read()
            file = json.loads(file)
            file.sort(key=lambda type: type['name'])
            return file

        def write(typelist):
            import json
            typelist.sort(key=lambda type: type['name'])
            typelist = json.dumps(typelist)
            file = open(f'{pokefiles.path}\\data\\storage\\typing.json', 'w')
            file.write(typelist)
