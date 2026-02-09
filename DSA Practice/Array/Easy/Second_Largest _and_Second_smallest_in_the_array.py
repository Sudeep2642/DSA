#function to find the second smallest element in the array
def sSmallest(arr, n):
    #edge case: if the array is empty or is less than 2 elements
    if n < 2:
        return -1
    
    small = float('inf')
    second_small = float('inf')

    # loop through the array to find the smallest and second smallest element in the array
    for i in range(n):
        if arr[i] < small:
            second_small = small
            small = arr[i]
        elif arr[i] < second_small and arr[i] != small:
            second_small = arr[i]
    return second_small

# function to find the second largest element in the array
def secondLargest(arr, n):
    #edge case if the array is empty or is less than 2 elements
    if n < 2:
        return -1
    
    large = float('-inf')
    sLarge = float('-inf')

    for i in range(n):
        if arr[i] > large:
            sLarge = large
            large = arr[i]
        elif arr[i] > sLarge and arr[i] != large:
            sLarge = arr[i]
    return sLarge

#Driver code
if __name__ == "__main__":
    arr = [1, 2, 4, 7, 7, 5] 
    n = len(arr)

    #to find the second smallest and second largest element in the array
    sS = sSmallest(arr, n)
    sL = secondLargest(arr, n)

    print(f"Second smallest element in the array is: {sS}")
    print(f"Second largest element in the array is: {sL}")


