class Ability:
  def __init__(ability, data):
    ability.name = data['name']
    ability.effect = data['effect']
    ability.activation = data['activation']

  def new():
    from utilities.responses import response
    addnew = input('add new ability?\n')
    data = []
    while addnew not in response.polar.valid:
      addnew = input('add new ability?\n')
    while addnew in response.polar.yes:
      name = input('ability name: ')
      effect = input('ability effect: ')
      activation = input('activated by: ')
      ability = {'name': name, 'effect': effect, 'activation': activation}
      data.append(ability)
      addnew = input('add new ability?\n')
    return data
