#optimal Soln:
class Solution:
    def rotateArrayByOne(self, nums):
        temp = nums[0]
        for i in range(1, len(nums)):
            nums[i - 1] = nums[i]
        nums[-1] = temp

if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    print(nums)
