string = input("Enter a letter:")
str = string.upper()
if str == str[::-1]:
    print("The letter is a palindrome")
else:
    print("The letter is not a palindrome")

# using recursion
n = int(input("please give a number : "))


def reverse(num):
    if num < 10:
        return num
    else:
        return int(str(num % 10) + str(reverse(num // 10)))


def isPalindrome(num):
    if num == reverse(num):
        return 1
    return 0


if isPalindrome(n) == 1:
    print("Number is a palindrome")
else:
    print("Number is not a palindrome number")
