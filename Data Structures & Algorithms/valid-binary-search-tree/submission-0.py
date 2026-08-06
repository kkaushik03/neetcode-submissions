class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue = deque()
        queue.append((root, float('-inf'), float('inf')))
        while queue:
            element, low, high = queue.popleft()
            if not (low < element.val < high):
                return False
            if element.left:
                queue.append((element.left, low, element.val))
            if element.right:
                queue.append((element.right, element.val, high))
        return True