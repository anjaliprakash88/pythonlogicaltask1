x = int(input("enter a number: "))
while x > 0:
    j = x % 10
    if j != 1 and j != 0:
        print("not the correct binary representation")
        break
    x = x // 10
if x == 0:
    print("binary")