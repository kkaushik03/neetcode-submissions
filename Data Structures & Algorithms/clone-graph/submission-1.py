"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:        # ADD at top
            return None
        visited = set()
        clone = {}
        stack = deque()
        stack.append(node)
        clone[node] = Node(node.val)
        while(stack):
            n = stack.pop()
            for neighbor in n.neighbors:
                if neighbor not in clone:
                    clone[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)
                clone[n].neighbors.append(clone[neighbor])     
        return clone[node]

        
        