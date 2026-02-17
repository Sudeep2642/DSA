#Optimal solution for union of two sorted arrays
class Solution:
    def FindUnion(self arr1, arr2, n, m):
        i, j = 0, 0
        union = []
        
        while i < n and j < m:
            if arr1[i] < arr2[j]:
                if not union or union[-1] != arr1[i]:
                    union.append(arr1[i])
                i += 1
            elif arr1[i] > arr2[j]:
                if not union or union[-1] != arr2[j]:
                    union.append(arr2[j])
                j += 1
            else:
                if not union or union[-1] != arr1[i]:
                    union.append(arr1[i])
                i += 1
                j += 1
        
        while i < n:
            if not union or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
        
        while j < m:
            if not union or union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1
        
        return union
    
#Driver Code
arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [ 1, 2, 3, 4, 4, 5, 6, 11, 12]
n, m = len(arr1), len(arr2)
sol = Solution()
result = sol.FindUnion(arr1, arr2, n, m)
print("Union of the two arrays is:", result)