import pdb

class Hash_me(object):
    def __init__(self, *args):
        if len(args) % 2 != 0:
            raise  RuntimeError ("Hash takes only an even amount of arguments")
        self.bin_count = 10
        self.bins = [None] * 10 #Create an empty list with 10 slots. 
        for idx, val in enumerate(args):
            arr = args
            if idx < len(arr) - 1 and (idx == 0 or idx % 2 == 0): #accept only arguments with an even index as keys
                index = self.init_idx(arr[idx])
                try:
                    self.bins[index] = [arr[idx], arr[idx+1]]
                except IndexError:
                    self.bins.insert(index, [arr[idx], arr[idx+1]])

    # create __iter__ and __next__ methods to make class enumerable
    def __iter__(self):
        return iter(self.bins)

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

    #setter and getters
    def set_bin_count(self, value):
        self.__bin_count = value
       
    def get_bins(self):
        return self.__bins

    def set_bins(self, value):
        self.__bins = value

    def get_bin_count(self):
        return self.__bin_count

    def double_bins(self):
        bin_len = len(self.bins)
        for num in range(bin_len):
            self.bins.append(None)


    #calculate and store in first available empty slot and key, value in 
    def add(self, key, value):
        index = self.init_idx(key)
        self.bins[index] = [key, value]


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

    #iterate through merging hash, if slot in self empty, copy item, else, go through add method    
    def merge(self, entry):
        for index, item in enumerate(entry):
            if item != None: 
                if self.bins[index] == None:
                    self.bins[index] = item
                    return self
                else:
                    self.add(item[0], item[1])
                    return self

    def rehash(self):
        new_bins = [None] * self.bin_count * 2
        self.bin_count = self.bin_count * 2
        for binn in self.bins:
            if binn != None:
                index = self.new_idx(binn[0], new_bins)
                new_bins[index] = [binn[0], binn[1]]
                print new_bins
        self.bins = new_bins
        self.bin_count = len(self.bins)


    def new_idx(self, key, li):    
        index = self.bin_for(key)
        while True:
            if li[index] == None: # Get an empty slot at said index, else, see if the next slot is empty
                return index
            else:  
                index += 1 


    #wrapper around hashing algo to prevent collisions
    def init_idx(self, key):
        if self.bins.count(None) < self.bin_count / 2:  # if you are running out of slots in the array double it
            self.rehash()
        return self.new_idx(key, self.bins)

    # Check if key is at said index, otherwise check next slot
    def get_idx(self, key):
        index = self.bin_for(key)
        bin_len = self.bin_count
        while True: 
            if self.bins[index] != None and self.bins[index][0] == key:
                return index
            else: 
                if index < bin_len - 1:
                    index += 1
                # else:
                #     bin_len = bin_len / 2
                #     index = bin_len
    #calculate the index to store and retrieve the pair of values
    def bin_for(self, key):
        return hash(key) % self.bin_count 

    bin_count = property(get_bin_count, set_bin_count)
    bins = property(get_bins, set_bins)


