# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = [] 
        if not root:
            return 0
        stack = deque() #assuming the root is the highest value. 
        stack.append((root,root.val))
        result = []
        result.append(root.val)
        while stack:
            element,maxi = stack.pop()
            if element.left: 
                stack.append((element.left,max(element.left.val,maxi)))
                if element.left.val>=maxi: 
                    result.append(element.left.val)
            if element.right: 
                stack.append((element.right,max(element.right.val,maxi)))  
                if element.right.val>=maxi: 
                    result.append(element.right.val) 

        return len(result) 
