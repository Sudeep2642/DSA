# Brute force approach to find GCD
def find_gcd(a, b):
    gcd = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd
# Example usage
a = 48
b = 18      
gcd = find_gcd(a, b)
print(f"The GCD of {a} and {b} is: {gcd}")  

# optimal approach using Euclidean algorithm
def gcd_euclidean(a, b):    
    while b:
        a, b = b, a % b
    return a        
# Example usage
a = 48      
b = 18
gcd = gcd_euclidean(a, b)
print(f"The GCD of {a} and {b} using Euclidean algorithm is: {gcd}")