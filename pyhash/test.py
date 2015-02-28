import pdb

bins = [1,2,5,'empty',8,9,'empty']
keys = []

def do_it(bins, keys):
    for item in bins:
        if item != 'empty':
            pdb.set_trace()
            keys.append(item)
            print keys

do_it(bins, keys)


# def add(seq):
#   total = 0
#   for item in seq:
#     total = total + item
#   return total


# def fib_sum(n):
#   fib_list = [0] * n

#   fib_list[0] = 0
#   fib_list[1] = 1

#   for i in range(2, n):
#     pdb.set_trace()
#     fib_list[i] = fib_list[i-2] + fib_list[i-1]

#   total = add(fib_list)
#   return total


# if __name__ == '__main__':
#   print fib_sum(10)