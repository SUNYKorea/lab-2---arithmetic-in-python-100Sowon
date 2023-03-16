# -------------------------------------- Task 1 -----------------------------------
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def div(a, b):
    return a / b

def multi(a, b):
    return a * b

def exp(a, b):
    return a ** b

# TODO: Add definitions of sub(), div(), mult(), exp(), as well as neg() and sqrt().
#       neg() should return the negation of the given number, and sqrt() should
#       return the square root of the given number. 

def neg(a):
   return -a# fill here

def sqrt(a):
    return a ** 0.5 # fill here

# -------------------------------------- Task 2 -----------------------------------

# TODO: Implement the quadratic formula using *only* the functions defined here.
#       Do not use arithmetic operators directly. 
#       You're allowed to define other functions.
a = 1
b = -3
c = 1

x1 = div(add(neg(b),sqrt(sub(exp(b, 2), multi(multi(4,a),c)))),multi(2,a)) # TODO: write a code to compute the first root of the quadratic equation
x2 = div(sub(neg(b),sqrt(sub(exp(b, 2), multi(multi(4,a),c)))),multi(2,a)) # TODO: then do the same for the second root
# Note: Make sure to remove the ellipsis (...) when you're writing your code

print("First root:" + str(x1))
print("Second root:" + str(x2))