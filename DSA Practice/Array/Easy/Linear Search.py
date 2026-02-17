#Linear Search
def linearSearch(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i
        
arr = [1, 2, 3, 4, 5, 6, 6]
num = 5
result = linearSearch(arr, num)
if result is not None:
    print(f"Element found at index: {result}")
else:  print("Element not found in the array.")