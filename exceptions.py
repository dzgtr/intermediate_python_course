# Errors and Exceptions
a = 5 print(a)))) # syntax error, no new line + unmatched parentheses
a = 5 + "10" # unsupported operand types, can't add int and string
import somemodule # module not found error
b = c # c is not defined
f = open("somefile.txt") # file not found error
a = [1,2,3]
a.remove(4) # value error, 4 not in list
a[4] # index error, list index out of range
mydict = {"name": "Max"}
mydict["age"] # key error
if x < 0:
    raise Exception("x should be positive")
assert (x>=0), "x is not positive" # raises AssertionError when the condition is false, doesn't need the text argument
try:
    a = 5 / 0 # normally gives zero division error, with try it does what expect: says
except:
    print("custom error") # except Exception as e: print(e) prints the division by zero error
try:
    a = 5 / 1
    b = a + "10"
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("no exceptions occured")
finally:
    print("cleaning operations") # happens every time

class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError("value is too high")
    if x < 5:
        raise ValueTooSmallError("value is too small", x)

try:
    test_value(200)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)