
class Solution:
    def search(self, A : list, l : int, h : int, key : int):
        # l: The starting index
        # h: The ending index, you have to search the key in this range
        # Complete this function
        if key not in A:
            return -1
        while l<h:
            if A[l]==key:
                return l
            if A[h]==key:
                return h
            l+=1
            h-=1
