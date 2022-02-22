class extract:
    def request_data(keys: list, data: object, return_list=False):
        """
        returns specified data from a request object as a dict or list
         return_list:
            False(default): returns a dictionary
            True: returns a list with only the values
        """
        if return_list:
            extracted = []
            for key in keys:
                try:
                    item = data[key]
                    if item == 'on':
                        item = True
                    extracted.append(item)
                except:
                    extracted.append(False)

        else:
            extracted = {}
            for key in keys:
                try:
                    item = data[key]
                    if item == 'on':
                        item = True
                    extracted.update({key: item})
                except:
                    extracted.update({key: False})

        return extracted

class generate:
    def digit_code(length: int):
        """
        returns a string of random integers
        """
        from random import randint
        code = ''
        while len(code) < length:
            digit = randint(0, 9)
            code += str(digit)
        return code

class retrieve:
    def patron(regcode:str=False):
        """
        Returns the Patron object matching the specified parameter or False
        """
        from PATRONS.models import Patron
        if regcode:
            patron = Patron.objects.filter(regcode=regcode)
            try:
                patron = patron[0]
            except:
                patron = False
        return patron

    def google_fonts():
        """
        returns a list of avaiable fonts from Google's API
        """
        import requests as api
        from .api_keys import GoogleFonts
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