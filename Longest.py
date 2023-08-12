from bisect import bisect_left
class Solution:
    
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,nums,n):
        arr = [nums[0]]
        for i in nums[1:]:
            if i>arr[-1]:
                arr.append(i)
            else:
                ind = bisect_left(arr,i)
                if ind < len(arr):
                    arr[ind] = i
        return len(arr)
