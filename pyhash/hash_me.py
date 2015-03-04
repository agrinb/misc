import pdb
import uuid

class Hash_me(object):
    def __init__(self, *args):
        if len(args) % 2 != 0:
            raise  RuntimeError ("Number of arguments must be even")
        if len(args) < 2:
            raise  RuntimeError("Hash takes at least two arguments")  
        self.bin_count = 10
        self.bins = [None] * 10
        for idx, val in enumerate(args):
            arr = args
            if idx < len(arr) - 1 and (idx == 0 or idx % 2 == 0):
                index = self.init_idx(arr[idx])
                try:
                    self.bins[index] = [arr[idx], arr[idx+1]]
                except IndexError:
                    self.bins.insert(index, [arr[idx], arr[idx+1]])


    def __iter__(self):
        return iter(self.bins)

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

    def set_bin_count(self, value):
        self.__bin_count = value
       

    def double_bins(self):
        bin_len = len(self.bins)
        for num in bin_len:
            self.bins.append(None)


    def get_bins(self):
        return self.__bins

    def set_bins(self, value):
        self.__bins = value

    def get_bin_count(self):
        return self.__bin_count

    def get(self, key):
        index = self.get_idx(key)
        return self.bins[index][1]
    

    def keys(self):
        keys = []
        for item in self.bins:
            if item != None:
                keys.append(item[0])
        return keys


    def values(self):
        values = []
        for item in self.bins:
            if item != None:
                values.append(item[1])
        return values

    def merge(self, entry):
        for index, item in enumerate(entry):
            if item != None: 
                if self.bins[index] == None:
                    self.bins[index] = item
                    return self
                else:
                    self.add(item[0], item[1])
                    return self

    def init_idx(self, key):
        bin_len = len(self.bins)
        # if you are running out of slots in the array double it
        if self.bins.count(None) < bin_len / 2:
            self.double_bins
        index = self.bin_for(key)
        while True:
            if self.bins[index] == None: # Get an empty slot at said index, else, see if the next slot is empty
                return index
            else:  
                index += 1 

    # Check if key is at said index, otherwise check next slot
    def get_idx(self, key):
        index = self.bin_for(key)
        while True: 
            if self.bins[index][0] == key:
                return index
            else: 
                index += 1

    #calculate the index to store and retrieve the pair of values
    def bin_for(self, key):
        return hash(key) % self.bin_count 

    bin_count = property(get_bin_count, set_bin_count)
    bins = property(get_bins, set_bins)



