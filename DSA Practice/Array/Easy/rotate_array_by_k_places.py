#Optimal Soln:
class Solution:
    #Helper function to reverse the part of array between two indices
    def reverse(self, nums, start, end):
        #Swap elements from start to end
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    #function to rotate the array to the left or right by k steps
    def rotateArray(self, nums, k, direction):
        n = len(nums)
        #edge cases
        if n == 0 or k == 0:
            return nums
        
        #normalize k if its larger than n
        k = k % n

        #if direction is right
        if direction == 'right':
            #step 1: reverse the entire array
            self.reverse(nums, 0, n - 1)
            #step 2: reverse the first k elements
            self.reverse(nums, 0, k - 1)
            #step 3: reverse the remaining n-k elements
            self.reverse(nums, k, n - 1)

        #if direction is left
        elif direction == 'left':
            #step 1: reverse the first k elements
            self.reverse(nums, 0, k - 1)
            #step 2: reverse the remaining n-k elements
            self.reverse(nums, k, n - 1)
            #step 3: reverse the entire array
            self.reverse(nums, 0, n - 1)

        return nums
    
#Driver Code
sol = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
direction = input("Enter the direction to rotate the array (left or right): ")
result = sol.rotateArray(nums, k, direction)
print(f"Array after rotating in {direction} direction by {k} steps: {result}")