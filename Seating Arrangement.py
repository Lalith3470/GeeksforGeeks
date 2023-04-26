from typing import List
class Solution:
    def is_possible_to_get_seats(self, n : int, m : int, seats : List[int]) -> bool:
        # code here
        seats.insert(0,0)
        seats.append(0)
        for i in range(1,len(seats)-1):
            if seats[i-1]+seats[i]+seats[i+1]==0:
                seats[i]=1
                n-=1
            if n==0:
                break
        
        return n<=0
        
