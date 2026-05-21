class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT ={}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
            
        return True
               

sol = Solution()
print(sol.isAnagram("anagram", "nagaram")) # True
print(sol.isAnagram("rat", "car")) # False

# Using Counter from collections module to simplify the code
from typing import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
    
sol = Solution()
print(sol.isAnagram("anagram", "nagaram")) # True  


# Using sorted function to compare the sorted strings
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
sol = Solution()
print(sol.isAnagram("anagram", "nagaram")) # True