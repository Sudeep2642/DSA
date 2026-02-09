
def largestElement(self, nums):
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
    return largest
nums = [26, 15, 16, 18, 24]
print(largestElement(None, nums))  # Output: 26
