#itertools: product, permutations, combinations, accumulate, groupby, infinite operators
from itertools import product
a = [1,2]
b = [3,4]
prod = product(a,b) # also has parameter repeat
print(list(prod)) # prod is a product object, with list() it prints [(1,3), (1,4), (2,3), (2,4)]

from itertools import permutations
a = [1,2,3]
print(list(permutations(a))) # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
permutations(a, 2) # only creates permutations of 2 numbers out of the list: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

from itertools import combinations, combinations_with_replacement
a = [1,2,3,4]
comb = combinations(a,2) # second argument is mandatory
print(list(comb)) # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
comb_wr = combinations_with_replacement(a,2) # does combinations with duplicate numbers
print(list(comb_wr)) # [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]

from itertools import accumulate
a = [1,2,3,4]
acc = accumulate(a)
print(list(acc)) # [1,3,6,10] - adds all previous numbers with current one
import operator
acc = accumulate(a, func=operator.mul) # [1,2,6,24], multiplys old list by previous number in new list, next would be 120(a[4] = 5 * acc[3] which is 24)
a = [1,2,5,3,4]
acc = accumulate(a, func=max) # [1,2,5,5,5]

from itertools import groupby
a = [1,2,3,4]
group_obj = groupby(a, key=lambda x: x < 3) # has to have a key
for key, value in group_obj:
    print(key, list(value)) # True [1,2] \n False [3,4]

from itertools import count, cycle, repeat
for i in count(10):
    print(i)            # prints from 10 to infinity
a = [1,2,3]
for i in cycle(a):
    print(i)            # prints 1,2,3 infinitely
for i in repeat(1, 4):
    print(i)            # prints 1 four times
