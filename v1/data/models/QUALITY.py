class Quality:
  def __init__(quality, data):
    quality.name = data['name']
    quality.effect = data['effect']
    quality.activation = data['activation']

  def new():
    from utilities.responses import response
    addnew = input('add new quality?\n')
    data = []
    while addnew not in response.polar.valid:
      addnew = input('add new quality?\n')
    while addnew in response.polar.yes:
      name = input('quality name: ')
      effect = input('quality effect: ')
      activation = input('activated by: ')
      quality = {'name': name, 'effect': effect, 'activation': activation}
      data.append(quality)
      addnew = input('add new quality?\n')
    return data
