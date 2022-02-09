# takes in an integer as the length and returns a random code


def digit_code(length):
    from random import randint
    code = ''
    while len(code) < length:
        digit = randint(0, 9)
        code += str(digit)
    return code
