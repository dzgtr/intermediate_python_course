# Sets: unordered, mutable, no duplicates
myset = {1,2,3}
myset = {1,2,3,1,2} #will print {1,2,3}
myset = set([1,2,3])
myset = set("Hello") #will create unordered set {'o','l','H','e'}, letters in random order, no duplicate L's
myset = {} #creates empty dictionary, for empty set have to use myset = set()
myset.add(1)
myset.remove(1)
myset.discard(2) #removes element, if it's not in a set doesn't raise an error unlike .remove()
myset.clear()
myset.pop() #returns random element from the set and removes it

odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}
unions = odds.union(evens) #combine two sets without duplication
intersection = odds.intersection(primes) #prints all items that are in both sets(AND)
diff = evens.difference(primes) #returns evens set without the elements that are in primes set - {0, 8, 4, 6}
sym_diff = evens.symmetric_difference(primes) #returns all elements that are not in both sets - {0, 3, 4, 5, 6, 7, 8}
odds.update(evens) #adds evens set to odds set without duplicates {1 to 9}
odds.intersection_update(primes) #updates the set only found in both sets {3,5,7}
odds.difference_update(primes) #removes the elements found in another set {1,9}
odds.symmetric_difference_update(primes) #keeps the elements only found in one of the sets but not both {1,2,9}

set1 = {1,2}
set2 = {1,2,3,4,5}
set1.issubset(set2) # returns True because all elements in set1 are in set2 = subset
set2.issuperset(set1) # returns True, set2 contains all elements that set1 has
set1.isdisjoint(set2) # returns False, sets contain same elements

# copying same as list/dict
myset_copy = myset #!! DOESN'T copy the set, only a reference to the memory, modyfying the copy changes the original
myset_copy = myset.copy() #actually creates a copy
myset_copy = set(myset) #same as above

frozen = frozenset([1,2,3,4]) # frozenset is a set that cannot be changed (like tuple set?)