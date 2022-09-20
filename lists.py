# Lists: ordered, mutable, allows duplicate elements
mylist = []
mylist = list()
mylist[-1] #last item in list, -2 for 2nd last etc.
len(mylist) #length of the list
mylist.append("item") #puts item in the end of the list
mylist.insert(0, "item") #puts item in the beginning of the list, moves others to the right
mylist.pop(0) #removes item on index 0 from the list, all items above it shifts to the left
mylist.remove("item") #removes specific item from the list, not working with index
mylist.clear() #clears the list
mylist.reverse() #reverses the list
mylist.sort() #sorts the list, new_list = sorted(mylist) doesn't change the original list
mylist = [0] * 5 #creates [0, 0, 0, 0, 0]
mylist[1:5] #slicing, return mylist index 1 to 5 excluded, [4,6,2,1,7,9] returns [6,2,1,7]
mylist[::2] #returns list with every second item, [start:end:step], defaults [0:len(pole):1], step -1 reverses the list
listcopy = mylist # !! DOESN'T copy the list, only a reference to the memory, changing listcopy changes mylist
listcopy = mylist.copy() # Actually creates a copy of mylist
listcopy = list(mylist) # same as above
listcopy = mylist[:] #slicing from beginning to the end also creates copy of mylist

#list comprehension
mylist = [1,2,3,4,5]
squared = [i*i for i in mylist] #squared is [1,4,9,16,25], syntax is expression + for loop for the original list