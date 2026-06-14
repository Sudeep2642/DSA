class ArmStrong:
    def is_armstrong(self, n):
        sum = 0
        k = len(str(n))
        temp = n
        while temp > 0:
            digit = temp % 10
            sum += digit ** k
            temp //= 10
        return sum == n

n = int(input())
armstrong = ArmStrong()
if armstrong.is_armstrong(n):
    print("Armstrong")
else:
    print("Not Armstrong")

# Optimal approach to check if a number is an Armstrong number
class ArmStrong:
    def is_armstrong(self, n):
        k = len(str(n))
        sum_of_digits = sum(int(digit) ** k for digit in str(n))
        return sum_of_digits == n

n = int(input())
armstrong = ArmStrong()
if armstrong.is_armstrong(n):
    print("Armstrong")
else:
    print("Not Armstrong")