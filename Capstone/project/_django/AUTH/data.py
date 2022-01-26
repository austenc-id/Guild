from pathlib import Path
import json


PROJECT_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = f"{PROJECT_DIR}/_assets/data/"


def get_patrons():
    with open(f'{DATA_DIR}patrons.json') as file:
        file = file.read()
        patron_data = json.loads(file)
    return patron_data['patrons']


def get_patron(regcode):
    patrons = get_patrons()
    for patron in patrons:
        if patron['regcode'] == regcode:
            return patron
    return 'not found'
