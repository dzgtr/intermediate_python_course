# Tuple: ordered, immutable, allows duplicate elements
mytuple = ()
mytuple = ("mountain", 7, "lion")
mytuple = "mountain", 7, "lion" #also recognized as a tuple
mytuple = ("mountain",) # without the comma it's recognized as a string even with parentheses
mytuple = tuple(["mountain", 7, "lion"])
item = mytuple[0] #same as lists
mytuple[0] = "sea" #doesn't work, tuples are immutable

mytuple = ('a','p','p','l','e')
mytuple.count('p') #returns 2
mytuple.index('p') #returns 1, first index where it finds 'p'
mylist = list(mytuple) #creates list out of tuple, tuple(mylist) does the opposite
mytuple[2:5] #slicing same as lists, from index 2 to 5 which is excluded
mytuple[::2] #same as lists, from start to finish, step 2, every other element, -1 for last to first element

mytuple = "apple", 5, "lion"
fruit, number, animal = mytuple #unpack the tuple into variables but the number of variables have to match the tuple length

mytuple = (0,1,2,3,4)
i1, *i2, i3 = mytuple # i1 is first item, i3 is last item, i2 will be [1,2,3], list of everything between

# how tuples are smaller size ond disk and faster to work with
import sys
mylist = [0,1,2,"hello",True]
mytuple = (0,1,2,"hello",True)
print(sys.getsizeof(mylist), "bytes")
print(sys.getsizeof(mytuple), "bytes")

import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000))