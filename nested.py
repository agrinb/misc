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


arr = ['a', 'b', 'c']

arr2 = ['a', 'z', 'c']
arr3 = ['a', 'z', 'c']

dd = {'a' : {'b' : { 'g' : 1}}}
dd2 =  nested(dd, arr)
print "step 2"
print dd2
print nested(dd2, arr2)
print "step 3=================="
print nested(dd2, arr3)

