from pathlib import Path
import json


PROJECT_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = f"{PROJECT_DIR}/_assets/data/"

# access patron data json and return dictionary


def get_patrons():
    with open(f'{DATA_DIR}patrons.json') as file:
        file = file.read()
        patron_data = json.loads(file)
    return patron_data['patrons']

# filter patron data for specific patron, return patron or not found


def get_patron(regcode):
    patrons = get_patrons()
    for patron in patrons:
        if patron['regcode'] == regcode:
            return patron
    return 'not found'
