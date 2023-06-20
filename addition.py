# add two numbers without using Arithmetic Operator
def add(a, b):
    for i in range(1, b + 1):
        a = a + 1
    return a


sum = add(10, 32)
print(sum)
