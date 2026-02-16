#shift the zeroes to the end of the array
class Solution:
    #function to move the zeroes to the end of the array
    def moveZeroes(self, nums):
        #pointer to the first zero
        j = -1
        #find the zeroes first
        for i in range(len(nums)):
            if nums[i] == 0:
                j = i
                break
        
        #if no-zeroes found, return
        if j == -1:
            return
        
        #start from the next index of first zero
        for i in range(j + 1, len(nums)):
            #if current element is non zero
            if nums[i] != 0:
                #swap i and j
                nums[i], nums[j] = nums[j], nums[i]
                #move j to next index
                j += 1

#Driver code
sol = Solution()
nums = [ 0, 1, 2, 3, 2, 0, 0, 4, 5, 1]
sol.moveZeroes(nums)
print(" ".join(map(str, nums)))