class Type:
  def __init__(pType, data):
    pType.name = data['name']
    pType.interactions = data

  def new():
    from utilities.responses import response
    addnew = input('add new type?\n')
    data = []
    while addnew not in response.polar.valid:
      addnew = input('add new type?\n')
    while addnew in response.polar.yes:
      name = input('type name: ')
      ptype = {'name': name}
      data.append(ptype)
      addnew = input('add new type?\n')
    return data
