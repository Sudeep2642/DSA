class solution:
    def twoSum(self, nums, target):
        hashMap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashMap:
                return [hashMap[complement], i]
            hashMap[nums[i]] = i
        return []

if __name__ == "__main__":
    sol = solution()       
    print(sol.twoSum([2, 6, 5, 8, 11], 14)) # [1, 3]

# time complexity: O(n) - we traverse the list once
# space complexity: O(n) - in the worst case, we store all elements in the