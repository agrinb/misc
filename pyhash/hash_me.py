import pdb

class Hash_me(object):
    def __init__(self):
        self.current = 0 
        self.high = 499
        self.bin_count = 500
        self.bins = ['empty'] * 500

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

    def get_bins(self):
        return self.__bins

    def set_bins(self, value):
        self.__bins = value

    def get_bin_count(self):
        return self.__bin_count

    def get(self, key):
        index = self.bin_for(key)
        return self.bins[index][1]

    def add(self, key, value):
        index = self.bin_for(key)
        try:
            self.bins[index] = [key, value]
        except IndexError:
            self.bins.insert(index, [key, value])
        return 

    

    def keys(self):
        keys = []
        for item in self.bins:
            if item != 'empty':
                keys.append(item[0])
        return keys



    def values(self):
        values = []
        for item in self.bins:
            if item != 'empty':
                values.append(item[1])
        return values

    def merge(self, entry):
        for index, item in enumerate(entry):
            if item != 'empty':
                if self.bins[index] == 'empty':
                    self.bins[index] = item
                    return self
                else:
                    self.add(item[0], item[1])
                    return self



    def bin_for(self, key):
        return id(key) % self.bin_count 

    bin_count = property(get_bin_count, set_bin_count)
    bins = property(get_bins, set_bins)


# ha = Hash_me()
# ha.add(8,9)
# ha2 = Hash_me()
# ha2.add(55,66)
# ha.merge(ha2)
# print ha.keys()