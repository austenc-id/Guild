def get_patron(regcode):
    from PATRONS.models import Patron
    patron = Patron.objects.filter(regcode=regcode)
    try:
        patron = patron[0]
    except:
        patron = False
    return patron


def get_google_fonts():
    import requests as api
    from utils.api_keys import GoogleFonts
    url = f'https://www.googleapis.com/webfonts/v1/webfonts?key={GoogleFonts}'
    response = api.get(url)
    count = 0
    json = response.json()  # .keys() = ['kind', 'items']
    items = json['items']
    fonts = []
    for item in items:
        font = (item['family'], item['family'])
        fonts.append(font)
    return fonts
