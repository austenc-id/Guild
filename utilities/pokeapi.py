import requests as req


class typing:
  def getdata():
    url = 'https://pokeapi.co/api/v2/type'
    res = req.get(url)
    data = res.json()
    data = data['results']
    exclude = ['unknown', 'shadow']
    typinglist = []
    for typing in data:
      name = typing['name']
      if name not in exclude:
        url = typing['url']
        res = req.get(url)
        typedata = res.json()
        interactions = typedata['damage_relations']
        strengths = interactions['half_damage_from']
        strengthlist = []
        for strength in strengths:
          strength = strength['name']
          strengthlist.append(strength)
        weaknesses = interactions['double_damage_from']
        weaknesslist = []
        for weakness in weaknesses:
          weakness = weakness['name']
          weaknesslist.append(weakness)
        immunities = interactions['no_damage_from']
        immunitylist = []
        for immunity in immunities:
          immunity = immunity['name']
          immunitylist.append(immunity)
        typing = {'name': name, 'strengths': strengthlist,
                  'weaknesses': weaknesslist, 'immunities': immunitylist}
        typinglist.append(typing)
    data = typinglist
    return data
