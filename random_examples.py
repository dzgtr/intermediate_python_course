import random
a = random.random() # random float from 0 to 1
a = random.uniform(1, 10) # random float from 1 to 10
a = random.randint(1, 10) # random integer from 1 to 10, both 1 and 10 are included
a = random.randrange(1, 10) # same as above but with range so 10 is not included
a = random.normalvariate(0,1) # random from normal distribution
mylist = list("ABCDEFGH")
a = random.choice(mylist) # one random element from list
a = random.sample(mylist, 3) # pick three random but unique elements from list, no duplicates
a = random.choices(mylist, k=3) # same as above but can choose an element multiple times
random.shuffle(mylist) # shuffle list
random.seed(1) # using the same seed reproduces the same results, same as creating a world in minecraft

import secrets
a = secrets.randbelow(10) # random number in range(0, 10)
a = secrets.randbits(4) # random number 4 bits long(0000 to 1111, 0 to 15 in decadic)
mylist = list("ABCDEFGH")
a = secrets.choice(mylist) # same as random.choice but not reproducable

import numpy as np
a = np.random.rand(3) # 1D array with 3 random floats
a = np.random.rand(3,3) # 2D array with 9 random floats
a = np.random.randint(0, 10, 3) # 1D array with 3 random integers
a = np.random.randint(0, 10, (3, 3)) # 2D array with 9 random integers
arr = np.array([[1,2,3], [4,5,6], [7,8,9]]) # array with custom numbers
np.random.shuffle(arr) # only switches the arrays on the Y axes, [1,2,3] with [4,5,6] etc, not the elements inside
print(arr)
np.random.seed(1) # reproducable, same as random, same as minecraft