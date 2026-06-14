class Solution:
    def findDivisors(self, n: int) -> list[int]:
        divisors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
        return sorted(divisors)

sol = Solution()
n = int(input("Enter a number: "))
divisors = sol.findDivisors(n)
print(f"The divisors of {n} are: {divisors}")