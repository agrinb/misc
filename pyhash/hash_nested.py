def nested(dct, li):
    hkey = li.pop(0)
    if hkey in dct and type(dct[hkey]) == dict: # if hash has a key that is associated with array 
        nested(dct[hkey], li)  #recurse with moded array
    elif len(li) == 0: # if array is on it's last variable
        if hkey in dct.keys():  #if last child exists
            dct[hkey] += 1 #add 1
        else:
            return dct.update({hkey: 1}) # create child with value of 1
    else:
        dct.update({hkey: {}}) #create hash with and empty value
        nested(dct[hkey], li)  #descend into newly created hash
    return dct

