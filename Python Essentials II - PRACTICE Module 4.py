"""
from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

###
###
###

def outer(par):
    loc = par

    def inner():
        return loc
    return inner

var = 1
fun = outer(var)
print(fun())

#
#
#
my_tuple = (0,1,2,3,4,5,6)
foo = list(filter(lambda x: x-0 and x-1, my_tuple))
print(foo)

#
#
#
my_list = [1,2,3]

for v in range(len(my_list)):
    print(v)
    print(my_list)
    my_list.insert(1,my_list[v])

print(my_list)

#
#
#
a=1
b=0
a= a^ b
print(a)
b=a^b
print(b)
a=a^b
print(a,b)

lst = [i for i in range(-1,-2)]
print(lst)

top = (1,2,4,8)
top = top[-2:-1]
top = top[-1]
print(top)

x = 3
y = 2
x = x % y
print(x)
x = x % y
print(x)
y= y % x
print(y)

###
class A:
    def __init__(self):
        pass

    def f(self):
        return 1

    def g():
        return self.f()


a = A()
print(a.g())

###
tup = (1,2,3)
lst = [1,2,3]

print(tup)

print(lst)

tup = (3,)

print(tup)

#
def fun(n):
    s = ''
    for i in range(n):
        s += '*'
        #print(s)
        yield s

for x in fun(3):
    print(x)

def a(x):
    def b():
        return x + x
    return b

x = a('x')
y = a('')
print(x() + y())

i=4

while 1 > 0:
    i -= 2
    print("*")
    if i == 2:
        break

else:
    print("*")

#
class A:
    def __init__(self,v=2):
        self.v = v + A.A
        A.A += 1

    def set(self,v):
        self.v += v
        A.A += 1
        return
a = A()
a.set(2)
print(a.v)

###

class A:
    def __init__(self, v):
        self._a = v + 1

a = A(0)
print(a._a)

###
try:
    raise Exception(1,3,2)
except Exception as ex:
     for i in ex.args:
        print(i)
###

try:
    raise Exception(1,3,2)
except:
    print('hello')
except Exception as ex:
    print('heelo')
"""

class A:
    B = 'test'
    def __init__(self):
        pass

inst = A()

print(inst.B)

print(A.B)

print(hasattr(inst,'B'))









