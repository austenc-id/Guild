def get_patron(regcode):
    from app_Patrons.models import Patron
    patron = Patron.objects.filter(regcode=regcode)
    try:
        patron = patron[0]
    except:
        patron = False
    return patron
