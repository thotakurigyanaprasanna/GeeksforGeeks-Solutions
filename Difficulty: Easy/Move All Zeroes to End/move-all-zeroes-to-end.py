class Solution:
	def pushZerosToEnd(self, arr):
    	# code here
    	idx=0
    	for i in range(len(arr)):
    	    if arr[i]!=0:
    	        arr[idx]=arr[i]
    	        idx+=1
    	for i in range(idx,len(arr)):
    	    arr[i]=0
    	return arr
