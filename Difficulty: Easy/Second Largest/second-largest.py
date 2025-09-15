class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        l=list(set(arr))
        l.sort()
        #print(l)
        if len(l)>=2:
            return l[-2]
        else:
            return -1