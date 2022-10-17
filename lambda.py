# lambda arguments: expression
add10 = lambda x: x + 10
print(add10(5)) # prints 15
mult = lambda x, y: x*y
print(mult(2,7)) # prints 14

points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D) # [(1, 2), (5, -1), (10, 4), (15, 1)] sorts by the first argument in tuple
points2D_sorted = sorted(points2D, key=lambda x: x[1]) # [(5, -1), (15, 1), (1, 2), (10, 4)] sorts by second argument
points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1]) # [(1, 2), (5, -1), (10, 4), (15, 1)] sorted by The SUMS of each tuple

#map(func, seq)
a = [1,2,3,4,5]
b = map(lambda x: x*2, a) # creates a map object
print(list(b)) # prints the map [2,4,6,8,10]
c = [x*2 for x in a] # does the same thing without map

#filter(func, seq), returns all elements for which the function evaluates True
a = [1,2,3,4,5,6]
b = filter(lambda x: x%2==0, a) # creates an object with list of only even numbers from a
print(list(b)) # [2, 4, 6]
c = [x for x in a if x%2==0] # does the same thing without filter

#reduce(func, seq)
from functools import reduce
a = [1,2,3,4]
product_a = reduce(lambda x, y: x*y, a) # multiplys all elements, 1*2*3*4 = 24
print(product_a)