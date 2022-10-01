# Dictionary: key-value pairs, unordered, mutable
mydict = {"name": "Jock", "age": 23, "city": "Hong Kong"}
mydict = dict(name="Jock", age=23, city="Hong Kong") #keys are passed as args
value = mydict["name"] # access value by key
mydict["address"] = "14th & Vine" #adds key and value to the dictionary, if adress is already used overwrites it
del mydict["address"] #deletes the key and value
mydict.pop("address") #same as delete but you can assing it to a variable with variable = mydict.pop(...)
mydict.popitem() #Python 3.7+ removes the last key:item in dictionary

if "name" in mydict: pass #True if key exists, can do try+except to check as well
for key in mydict: pass #goes through all keys, same as for key in mydict.keys()-returns list of keys
for value in mydict.values(): pass #goes through all the values in dictionary
for key, value in mydict.items():
    print(key, value)

mydict_copy = mydict #!! DOESN'T copy the dict, only a reference to the memory, modyfying the copy changes the original
mydict_copy = mydict.copy() #actually creates a copy
mydict_copy = dict(mydict) #same as above

mydict = {"name": "Jock", "age": 23, "adress": "14th & Vine"}
mydict2 = dict(name="James", age=46, city="London")
mydict.update(mydict2)  #overwrites mydict with mydict2, doesn't update the adress since there is none in mydict2

mydict = {1:1, 2:4, 3:9}
value = mydict[0]#Error as dicts are unordered there is no first value, have to specify the key (1, 2 or 3 in this case)

mytuple = (8, 7)
mydict = {mytuple: 15} #mydict is {(8, 7): 15}, you can use tuples as a key, but not lists as they are changeable(unhashable)