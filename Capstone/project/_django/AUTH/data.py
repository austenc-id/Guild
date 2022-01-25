from pathlib import Path
import json


PROJECT_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = f"{PROJECT_DIR}/_assets/data/"


def get_patrons():
    with open(f'{DATA_DIR}patrons.json') as file:
        file = file.read()
        patron_data = json.loads(file)
    return patron_data['patrons']


def extract_data(data):
    try:
        first = data['first_name']
        last = data['last_name']
        regcode = data['regcode']
    except:
        return 'invalid'
    else:
        return [first, last, regcode]


def get_patron(regcode):
    patrons = get_patrons()
    for patron in patrons:
        if patron['regcode'] == regcode:
            return patron
