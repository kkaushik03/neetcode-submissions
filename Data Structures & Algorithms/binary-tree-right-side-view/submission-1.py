# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque()
        visited = [] 
        queue.append(root)
        result = []
        while queue: 
            level_len = len(queue)
            for i in range (level_len): 
                element = queue.popleft()
                if i == level_len - 1:       # last node in this level = rightmost
                    result.append(element.val)
                if element.left:
                    queue.append(element.left)
                if element.right:
                    queue.append(element.right)
        return result

            
            


        