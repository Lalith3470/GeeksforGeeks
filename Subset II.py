class Solution:
    def printUniqueSubset(self, nums):
        # Code here
        lst,tmp=[],[]
        dic={}
        def subs(idx,nums,n,tmp,lst):
            if idx>=n:
                if str(tmp) not in dic:
                    dic[str(tmp)]=1
                    lst.append(tmp[:])
                return
            tmp.append(nums[idx])
            subs(idx+1,nums,n,tmp,lst)
            tmp.pop()
            subs(idx+1,nums,n,tmp,lst)
        nums.sort()
        subs(0,nums,len(nums),tmp,lst)
        return sorted(lst)
