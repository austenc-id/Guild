class Version:
    def __init__(version, data):
        version.name = data['name']
        version.dexids = data['dexids']
        version.gens = data['generations']
        version.pokedex = data['pokedex']
