class poke:
    def species(data):
        species = data.capitalize()
        return species

    def typing(data):
        if len(data) == 1:
            typing = f'a {data[0].name} type pokemon'
        elif len(data) == 2:
            typing = f'a {data[0].name} and {data[1].name} type pokemon'
        return typing

    def abilities(data):
        if len(data) == 1:
            abilities = f'ability: {data[0].name}'
        elif len(data) == 2:
            abilities = f'abilities: {data[0].name} or {data[1].name}'
        return abilities

    def print(data):
        species = poke.species(data.species)
        typing = poke.typing(data.typings)
        abilities = poke.abilities(data.abilities)
        print('\n', species)
        print('', typing)
        print('', abilities, '\n')
        return

    def printtyping(pokemon):
        species = poke.species(pokemon.species)
        print()
        if len(pokemon.immune) > 0:
            string = f'{species} is immune to '
            if len(pokemon.immune) == 1:
                string += pokemon.immune[0]
            elif len(pokemon.immune) == 2:
                string += pokemon.immune[0] + ' and ' + pokemon.immune[1]
            while len(pokemon.immune) > 3:
                popimmune = pokemon.immune.pop()
                string += popimmune + ', '
            if len(pokemon.immune) == 3:
                string += pokemon.immune[0] + ', ' + \
                    pokemon.immune[1] + ', and ' + pokemon.immune[2]
            string += ' type attacks.'
            print(string)
            print()
        else:
            print(f'{species} has no immunities.')
            print()
        if len(pokemon.quarter) > 0:
            string = f'{species} is very resistant to '
            if len(pokemon.quarter) == 1:
                string += pokemon.quarter[0]
            elif len(pokemon.quarter) == 2:
                string += pokemon.quarter[0] + ' and ' + pokemon.quarter[1]
            while len(pokemon.quarter) > 3:
                popresist = pokemon.quarter.pop()
                string += popresist + ', '
            if len(pokemon.quarter) == 3:
                string += pokemon.quarter[0] + ', ' + \
                    pokemon.quarter[1] + ', and ' + pokemon.quarter[2]
            string += ' type attacks.'
            print(string)
            print()
        if len(pokemon.half) > 0:
            string = f'{species} is resistant to '
            if len(pokemon.half) == 1:
                string += pokemon.half[0]
            elif len(pokemon.half) == 2:
                string += pokemon.half[0] + ' and ' + pokemon.half[1]
            while len(pokemon.half) > 3:
                popresist = pokemon.half.pop()
                string += popresist + ', '
            if len(pokemon.half) == 3:
                string += pokemon.half[0] + ', ' + \
                    pokemon.half[1] + ', and ' + pokemon.half[2]
            string += ' type attacks.'
            print(string)
            print()
        if len(pokemon.double) > 0:
            string = f'{species} is weak to '
            if len(pokemon.double) == 1:
                string += pokemon.double[0]
            elif len(pokemon.double) == 2:
                string += pokemon.double[0] + ' and ' + pokemon.double[1]
            while len(pokemon.double) > 3:
                popweak = pokemon.double.pop()
                string += popweak + ', '
            if len(pokemon.double) == 3:
                string += pokemon.double[0] + ', ' + \
                    pokemon.double[1] + ', and ' + pokemon.double[2]
            string += ' type attacks.'
            print(string)
            print()
        if len(pokemon.quadruple) > 0:
            string = f'{species} is very weak to '
            if len(pokemon.quadruple) == 1:
                string += pokemon.quadruple[0]
            elif len(pokemon.quadruple) == 2:
                string += pokemon.quadruple[0] + ' and ' + pokemon.quadruple[1]
            while len(pokemon.quadruple) > 3:
                popweak = pokemon.quadruple.pop()
                string += popweak + ', '
            if len(pokemon.quadruple) == 3:
                string += pokemon.quadruple[0] + ', ' + \
                    pokemon.quadruple[1] + ', and ' + pokemon.quadruple[2]
            string += ' type attacks.'
            print(string)
            print()
        return

    def printability(data):
        ability = data.name
        description = data.description
        ability = f'\n   {ability} - {description}\n'
        print(ability)
        return
