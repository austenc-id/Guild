def get_patron(regcode):
    from app_Patrons.models import Patron
    patron = Patron.objects.filter(regcode=regcode)
    try:
        patron = patron[0]
    except:
        patron = False
    return patron


def get_patron_API(regcode):
    import requests
    base_url = 'http://127.0.0.1:8000/api/'
    url = f'{base_url}patrons/{regcode}'
    response = requests.get(url)
    data = response
    print(data)
