def pallindrome(n):
    rev = 0
    temp = n
    while temp > 0:
        rev = rev * 10 + temp % 10
        temp //= 10
    return rev == n

n = int(input())
if pallindrome(n):
    print("Pallindrome")
else:
    print("Not Pallindrome") 