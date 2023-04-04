
class Solution:
    #Function to return the position of the first repeating element.
    def firstRepeated(self,arr, n):
        
        #arr : given array
        #n : size of the array
        if len(set(arr))==len(arr):return -1
        for i in range(n):
            if arr.count(arr[i])>1:
                return i+1
        return -1
