# Strings: ordered, immutable, text representation
mystring = "Hello World"
mystring = """Hello \
World"""                # multi line string but \ makes it's on one line
char = my_string[0] # first character of the string, -1 for last character, can't change my_string with that=immutable
substring = mystring[1:5] # literally same as list slicing but with chars, also can do steps, ::-1 reverses whole string
string1 + " " + string2 #connects
for i in mystring:    print(i) #prints each character on new line
if "ell" in mystring: pass # checks if a letter or a substring is in mystring
mystring = "      Hello World       "
mystring = mystring.strip() # removes additional spaces, method itself doesn't change the string, have to assing it
mystring.upper() #uppercase
mystring.lower() #lowercase
mystring.startswith("H") # If string starts with specified string returns True, else False
mystring.endswith("rld") # If string ends with specified string returns True, else False
mystring.find("lo") # returns index where it finds the first occurance of "lo", if it doesn't find anything returns -1
mystring.count("o") # counts number of specified elements in string, 0 if there is none
mystring.replace("World", "Universe") # replaces the first argument with second one, if not found-does nothing. Also doesn't change the string (like strip)

mystring = "how are you doing"
mylist = mystring.split() # [how, are, you, doing], default arg in split is " "
newstring = " ".join(mylist) # joins mylist with space, creates the original string again
mylist = ["a"] * 6 # ["a", "a", "a", "a", "a", "a"]
mystring = "".join(mylist) # "aaaaaa", much faster than: for item in mylist: mystring += item

#old ways
var = "tom"
mystring = "the variable is %s" % var # "the variable is tom", %d for integer, $f for float(default 6 decimal digits, %.2f for 2 decimal)
var2 = 36
mystring = "the variable is {}".format(var) #same as above, {:.3} prints first three characters of var
mystring = "the variable is {:.1} and {}".format(var, var2) # "the variable is t and 36"

#new way Python 3.6+ f-String
mystring = f"the variable is {var*2} and {var2}" # "the variable is tomtom and 36"