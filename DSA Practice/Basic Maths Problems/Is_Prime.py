# Brute force approach to check if a number is prime
def is_prime(n):
    cnt = 0
    for i in range(1, n + 1):
        if n % i == 0:
            cnt += 1
    return cnt == 2

n=int(input())
if is_prime(n):
    print("Prime")      
else:
    print("Not Prime")

# Optimal approach to check if a number is prime
def is_prime(n):
    cnt = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            cnt += 1
            if i != n // i:
                cnt += 1
    return cnt == 2

n=int(input())
if is_prime(n):
    print("Prime")  
else:
    print("Not Prime")