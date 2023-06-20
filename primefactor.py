x = int(input("enter a number: "))
i = 2
while x != 0:
    rem = x % i
    if rem == 0:
        x = x / i
        print(i)
    else:
        i = i + 1