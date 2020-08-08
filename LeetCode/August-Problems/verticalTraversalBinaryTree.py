# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.results = collections.defaultdict(list)
    
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        stack = [[0, 0, root]]
        
        while len(stack) != 0:
            x, y, top = stack.pop()
            self.results[x].append([-y, top.val])
            
            if top.left is not None:
                stack.append([x-1, y-1, top.left])
            if top.right is not None:
                stack.append([x+1, y-1, top.right])
        
        children = []
        for i in sorted(self.results.keys()):
            sortedChildren = []
            for j, val in sorted(self.results[i]):
                sortedChildren.append(val)
            children.append(sortedChildren)
        
        return children