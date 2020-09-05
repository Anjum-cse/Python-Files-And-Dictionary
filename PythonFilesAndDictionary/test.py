
## Write two functions, one called addit and one called mult. addit takes one number as an input and adds 5. mult takes one number as an input, and multiplies that input by whatever is returned by addit, and then returns the result.

def addit(a):
    add = a + 5
    return add


def mult(a):
    return a * addit(a)

print(addit(5))

## exmp

def square(x):
    return x*x

def g(y):
    return y + 3

def h(y):
    return square(y) + 3

print(g(h(2)))



