#Is Array sorted and rotated
def check(arr):
    n = len(arr)
    count = 0
    for i in range(1, n):
        if arr[i - 1] > arr[i]:
            count += 1
        if arr[-1] > arr[0]:
            count += 1
        return count <= 1
    
if __name__ == '__main__':
    arr = [ 3, 4, 5, 1, 2]
    print(check(arr))