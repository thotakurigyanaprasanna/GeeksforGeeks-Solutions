#User function Template for python3

class Solution:
    def productExceptSelf(self, arr):
        #code here
        n = len(arr)
        res = [1] * n
    
    # Step 1: Calculate prefix products
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= arr[i]
    
    # Step 2: Multiply by suffix products
        suffix = 1
        for i in range(n-1, -1, -1):
            res[i] *= suffix
            suffix *= arr[i]
    
        return res