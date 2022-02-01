def regcode():
    from random import randint
    regcode = ''
    while len(regcode) < 4:
        digit = randint(0, 9)
        regcode += str(digit)
    return regcode
