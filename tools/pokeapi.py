from requests import get


class request:
  url = 'https://pokeapi.co/api/v2/'

  def pokemon(dexid):
    url = request.url + f'pokemon/{dexid}'
    data = get(url)
    data = data.json()
    return data

  def typing(url):
    data = get(url)
    data = data.json()
    return data

  def ability(url):
    data = get(url)
    data = data.json()
    return data
