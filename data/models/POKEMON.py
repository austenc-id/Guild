class Pokemon:
    def __init__(pokemon, data):

        pokemon.id = data['id']
        pokemon.species = data['species']
        pokemon.typing = data['typing']
        pokemon.zero = []
        pokemon.quarter = []
        pokemon.half = []
        pokemon.double = []
        pokemon.quadruple = []
        pokemon.multipliers = pokemon.getmultipliers()
        pokemon.resistances = pokemon.getresistances()
        pokemon.abilities = data['abilities']

    def new():
        from utilities.responses import response
        addnew = input('add new pokemon?\n')
        data = []
        while addnew not in response.polar.valid:
            addnew = input('add new pokemon?\n')
        while addnew in response.polar.yes:
            dexid = input('species id: ')
            while True:
                try:
                    int(dexid)
                except:
                    dexid = input('species id: ')
                else:
                    dexid = int(dexid)
                    break
            species = input('species: ')
            typing = input('typing: ')
            typing = typing.split()
            abilities = input('ability name: ')
            abilities = abilities.split(',')
            pokemon = {'id': dexid, 'species': species,
                       'typing': typing, 'abilities': abilities}
            data.append(pokemon)
            addnew = input('add new pokemon?\n')
        return data

    def getmultipliers(pokemon):
        from data.pokefiles import pokefiles
        resistances = {}
        typinglist = pokefiles.typing.read()
        for typing in typinglist:
            typing = typing['name']
            resistances.update({typing: 1})
        for typing in pokemon.typing:
            for immunity in typing.immunity:
                resistances[immunity] *= 0
            for strength in typing.strengths:
                resistances[strength] *= 0.5
            for weakness in typing.weaknesses:
                resistances[weakness] *= 2
        return resistances

    def getresistances(pokemon):
        resistances = []
        for typing in pokemon.multipliers:
            value = pokemon.multipliers[typing]
            if value == 0:
                pokemon.zero.append(typing)
            elif value == 0.25:
                pokemon.quarter.append(typing)
            elif value == 0.5:
                pokemon.half.append(typing)
            elif value == 2:
                pokemon.double.append(typing)
            elif value == 4:
                pokemon.quadruple.append(typing)
        resistances.append({'immune': pokemon.zero})
        resistances.append({'quarter': pokemon.quarter})
        resistances.append({'half': pokemon.half})
        resistances.append({'double': pokemon.double})
        resistances.append({'quadruple': pokemon.quadruple})
        return resistances
