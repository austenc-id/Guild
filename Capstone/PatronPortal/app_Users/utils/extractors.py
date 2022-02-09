def dictionary(keys, data, return_list=False):
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
