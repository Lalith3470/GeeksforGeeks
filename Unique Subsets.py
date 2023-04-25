class Solution:
    
    #Function to find all possible unique subsets.
    def AllSubsets(self, arr,n):
        #code here
        dic={}
        def subs(idx,arr,lst,tmp):
            if idx>=len(arr):
                if str(tmp) not in dic:
                    lst.append(tmp[:])
                    dic[str(tmp)]=1
                return
            tmp.append(arr[idx])
            subs(idx+1,arr,lst,tmp)
            tmp.pop()
            subs(idx+1,arr,lst,tmp)
            
        lst=[]
        tmp=[]
        arr.sort()
        subs(0,arr,lst,tmp)
        return sorted(lst)
