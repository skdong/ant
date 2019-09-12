# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        node = root
        stack = list()
        nodes = list()
        over = dict()
        while node:
            if node.left and node.left not in over:
                stack.append(node)
                node = node.left
                over[node] = node
            elif node.right and node.right not in over:
                stack.append(node)
                node = node.right
                over[node] = node
            else:
                nodes.append(node.val)
                node = None
                if stack:
                    node = stack.pop()
        return nodes