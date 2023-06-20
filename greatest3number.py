def greatest(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3


x = int(input("enter any three number: "))
y = int(input())
z = int(input())
greatest_number = greatest(x, y, z)
print("greatest number is ", greatest_number)