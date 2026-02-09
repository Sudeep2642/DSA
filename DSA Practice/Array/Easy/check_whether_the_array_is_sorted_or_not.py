#to check whether the array is sorted or not in the array
#brute force method
def isSorted(arr, n):
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                return False
    return True

arr = [2, 5, 7, 3, 4, 1, 9, 2]
n = len(arr)
ans = isSorted(arr, n)
if ans:
    print("The array is sorted")
else:
    print("The array is not sorted")



#optimal soln
def isSorted(arr, n):
    for i in range(n):
        if arr[i] < arr[i-1]:
            return False
    return True

arr = [2, 5, 7, 3, 4, 1, 9, 2]
n = len(arr)
print("True" if isSorted(arr, n) else "False")
            