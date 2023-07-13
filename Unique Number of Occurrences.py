from typing import List
from collections import Counter
class Solution:
    def isFrequencyUnique(self, n : int, arr : List[int]) -> bool:
        # code here
        cnt=Counter(arr)
        return len(cnt.values())==len(set(cnt.values()))
        
