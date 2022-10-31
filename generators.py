def mygenerator():
    yield 1
    yield 2         # yield is return but each time the function is called it goes to the next non-yet returned yield
    yield 3

g = mygenerator()
# value = next(g)
# print(value)
# value = next(g)
# print(value)
# print(sum(g)) # prints 6, 1+2+3
print(sorted(g)) # sorted creates a sorted list out of the yields = [1,2,3]

def countdown(num):
    print("Starting")
    while num > 0:
        yield num
        num -= 1

cd = countdown(4)
value = next(cd)
print(value)
print(next(cd))
# -------------------------------------------------------------------------------------------------------
import sys

def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

print(firstn(10))
print(list(firstn_generator(10))) # same as line above, converting the object to a list
print(sum(firstn_generator(10)))
print(sys.getsizeof(firstn(100)))
print(sys.getsizeof(firstn_generator(100))) # generator is much smaller because it doesn't store all the values in itself
# -------------------------------------------------------------------------------------------------------
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a,b = b, a+b

fib = fibonacci(30)
for i in fib:
    print(i)
# -------------------------------------------------------------------------------------------------------
my_generator = (i for i in range(10) if i % 2 == 0)
print(list(my_generator))
for i in my_generator:
    print(i)

mylist = [i for i in range(10) if i % 2 == 0]
print(mylist)