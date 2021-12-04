print('adding all the ML related to fraud detection')

def sub(a,b):
    c= a - b
    return c

def add(a,b):
    c= a + b
    return c

def mul(a,b):
    d= a * b
    return d

def div(a,b):
    e = a / b
    return e

a = int(input('Enter the value of A : '))
b = int(input('Enter the value of B : '))
c = sub(a,b)
print('The value of C is : ',c)

c = sum(a,b)
print('The value of C is : ',c)

d = mul(a,b)
print('The value of C is : ',d)

e = div(a,b)
print('The value of C is : ',e)

