from typing import List
from queue import Queue
from collections import deque
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        queue=deque()
        queue.append(0)
        visited=[0]
        while queue:
            tmp=queue.popleft()
            for i in adj[tmp]:
                if i not in visited:
                    queue.append(i)
                    visited.append(i)
        return visited
                
