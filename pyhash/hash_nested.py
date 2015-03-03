def nested(dct, li):
    hkey = li.pop(0)
    if hkey in dct and type(dct[hkey]) == dict:
        nested(dct[hkey], li)
    elif len(li) == 0:
        if hkey in dct.keys():
            dct[hkey] += 1
        else:
            return dct.update({hkey: 1})
    else:
        dct.update({hkey: {}})
        nested(dct[hkey], li)
    return dct

    