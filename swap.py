# with third variable

x = int(input("enter any two number: "))
y = int(input())
print("before Swapping")
print(" first number: ", x, "\n", "second number", y)
x = x + y
y = x - y
x = x - y
print("After Swapping")
print(" first number: ", x, "\n", "second number", y)

# without third variable

x, y = 12, 13
print("before Swapping")
print(" first number: ", x, "\n", "second number", y)
x, y = y, x
print("After Swapping")
print(" first number: ", x, "\n", "second number", y)
