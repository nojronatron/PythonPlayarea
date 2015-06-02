__author__ = 'Orange'
# Stuff about Classes
# Classes will have variables and functions
# A Class is a reference type

class demo(object):
    var1 = 5
    def myfunction(self):
        print('asdf')

# Access the stuff inside the Class "demo"
v1 = demo()
print(v1.var1)

# modify the object/class for your own use
v2 = demo()
v2.var1 = 10
print(v2.var1)

# IS operator compares objects to see if they are the same or different
if(v1 is v2):
    print("true")
else:
    print("false")

# Try the same Comparison Operator vs. ValueTypes
w1 = "four"
w2 = "five"
w1 = w2

if(w1 == w2):
    print("true")
else:
    print("false")

if(w1 is w2):
    print("true")
else:
    print("false")
