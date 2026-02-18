#Optimal solution to find the missing number in the array
#1st Approach: using the formula for the sum of first n natural numbers
def missingNum(arr):
    n = len(arr) + 1
    totalSum = sum(arr) #Calculate the sum of given array
    expSum = n * (n + 1) //2  #Calculate the expected sum of first n natural numbers
    result = expSum - totalSum #to find the missing number
    return result

if __name__ == '__main__':
    arr = [ 1, 2, 3, 4, 6, 7, 8]
    print(missingNum(arr))


#2nd Approach: using XOR operation
def missingN(arr1):
    n = len(arr1) + 1
    xor1 = 0
    xor2 = 0

    #XOR of all the elements in the array
    for i in range(n - 1):
        xor2 ^= arr1[i]

    #XOR all numbers from 1 to n
    for i in range(1, n +1):
        xor1 ^= i

    #Missing number is the XOR of xor1 and xor2
    res = xor1 ^ xor2
    return res

if __name__ == '__main__':
    arr1 = [ 1, 2, 3, 4, 5, 7, 8]
    print(missingN(arr1))
