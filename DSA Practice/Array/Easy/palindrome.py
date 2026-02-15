def palindrome(n):
    temp = n
    rev = 0
    while n > 0:
        if rev == rev * 10 + n % 10
        n = n / 10

    if rev == temp:
        return True
    else:
        return False  


n = int(input("Enter a number: "))
print(palindrome(n))
