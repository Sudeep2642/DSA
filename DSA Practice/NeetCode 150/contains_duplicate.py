class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.containsDuplicate([1,2,3,1])) # True
    print(sol.containsDuplicate([1,2,3,4])) # False
        