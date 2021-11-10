class Typing:
  def __init__(typing, data):
    typing.name = data['name']
    typing.strengths = data['strengths']
    typing.weaknesses = data['weaknesses']
    typing.immunity = data['immunities']

  def new():
    from utilities.responses import response
    addnew = input('add new type?\n')
    data = []
    while addnew not in response.polar.valid:
      addnew = input('add new type?\n')
    while addnew in response.polar.yes:
      name = input('type name: ')
      typing = {'name': name}
      data.append(typing)
      addnew = input('add new type?\n')
    return data
