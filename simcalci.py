def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    return a / b
choice = int(input('Enter choice = '))
a = int(input('Enter a = '))
b = int(input('Enter b = '))
if choice == 1 :
    print(add(a,b))
if choice == 2 :
    print(sub(a,b))
if choice == 3 :
    print(mul(a,b))
if choice == 4 :
    print(div(a,b))
elif choice > 4 :
    print('Enter correct choice')
