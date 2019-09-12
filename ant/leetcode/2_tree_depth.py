# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        stack = list([None])
        recorde = dict()
        node = root
        while node:
            if node.left and node.left not in recorde:
                stack.append(node)
                node = node.left
                recorde[node] = node
            elif node.right and node.right not in recorde:
                stack.append(node)
                node = node.right
                recorde[node] = node
            else:
                if depth < len(stack):
                    depth = len(stack)
                node = stack.pop()
        return depth
