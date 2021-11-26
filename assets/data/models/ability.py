class Ability:
  def __init__(ability, data):
    ability.name = data['name']
    ability.description = data['effect']
