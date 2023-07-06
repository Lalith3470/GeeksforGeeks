class Solution:
    def nextPermutation(self, N, nums):
        # code here
        x=0
        a=nums[::-1]
        for i in range(len(a)-1):
            if a[i]>a[i+1]:
                x=i+1
                break
        x=len(nums)-x-1
        y=len(nums)-1
        for i in range(x+1,len(nums)):
            if nums[x]>=nums[i]:
                y=i-1
                break
        if x==y and x==len(nums)-1:
            return nums[::-1]
        else:
            nums[x],nums[y]=nums[y],nums[x]
            rvs=nums[x+1:]
            return nums[:x+1]+rvs[::-1]
