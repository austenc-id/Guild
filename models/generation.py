class Generation:
  def __init__(gen, data):
    gen.name = data['name']
    gen.region = data['region']
    gen.start = data['start']
    gen.end = data['end']
