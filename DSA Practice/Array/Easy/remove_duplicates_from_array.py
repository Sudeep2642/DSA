#Brute Force
class solution:
    def removeDuplicates(self, nums):
        #set to store unique elements
        seen = set()
        #position to overwrite the next unique element
        index = 0
        #loop
        for num in nums:
            if num not in seen:
                seen.add(num)
                nums[index] = num
                index += 1
        return index
    
#Driver code
nums = [1, 1, 2, 2, 3, 4, 4, 5]
sol = solution()
k = sol.removeDuplicates(nums)
print("k=", k)
print("Unique elements in the array:", nums[:k])


#Optimal solution
class solution:
    def removeDuplicates(self, nums):
        #if list is empty
        if not nums:
            return 0
        i = 0 #pointer to keep track of the position of the last unique element
        for j in range(1, len(nums)):
            if nums[j] != nums[i]: #if the current element is not equal to the last unique element
                i += 1 #move the pointer to the next position
                nums[i] = nums[j] #update the position with the current unique element
        return i + 1 #return the number of unique elements in the array
    
nums = [1, 1, 2, 2, 3, 4, 4, 5]
sol = solution()
k = sol.removeDuplicates(nums)
print("k=", k)
print("Unique elements in the array:", nums[:k])