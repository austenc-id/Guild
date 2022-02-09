def dictionary(keys, data):
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
